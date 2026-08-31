#!/usr/bin/env python3
"""
ARK 续航与太阳能仿真模型
可调参数：使用模式、太阳能板功率、电池容量
"""

BATTERY_CAPACITY_MAH = 4500  # mAh
BATTERY_VOLTAGE = 3.85  # V (OnePlus 8T 典型电压)
BATTERY_ENERGY_WH = BATTERY_CAPACITY_MAH * BATTERY_VOLTAGE / 1000  # ~17.3 Wh

# 功耗模型（瓦特）
POWER_MODELS = {
    'idle': 0.5,
    'reading': 1.5,
    'ai_inference': 7.0,
    'mixed': 3.0,
}

# 太阳能板实际充电功率（瓦特），考虑转换效率 ~60%
SOLAR_PANELS = {
    '5W': 3.0,
    '10W': 6.0,
    '20W': 12.0,
}


def estimate_runtime(power_w, battery_wh=BATTERY_ENERGY_WH):
    """估算纯电池续航（小时）"""
    if power_w <= 0:
        return float('inf')
    return battery_wh / power_w


def estimate_self_sustain_days(solar_w, daily_power_wh, battery_wh=BATTERY_ENERGY_WH):
    """
    估算离线自持天数
    如果太阳能日发电量 >= 日耗电量，则无限自持
    """
    if solar_w >= daily_power_wh / 24 * 12:  # 假设每天日照 12 小时
        return float('inf')
    daily_consumption = daily_power_wh
    daily_generation = solar_w * 12  # 12 小时日照
    net_daily = daily_consumption - daily_generation
    if net_daily <= 0:
        return float('inf')
    return battery_wh / net_daily


def simulate_day(solar_w, usage_profile, battery_wh=BATTERY_ENERGY_WH):
    """
    模拟一天的能量平衡
    usage_profile: list of (hours, power_w) tuples
    """
    total_consumption = 0
    for hours, power in usage_profile:
        total_consumption += hours * power

    solar_generation = solar_w * 12  # 12 小时日照
    net = total_consumption - solar_generation

    return {
        'consumption_wh': total_consumption,
        'solar_generation_wh': solar_generation,
        'net_wh': net,
        'self_sustaining': net <= 0,
    }


def print_report():
    print("=" * 60)
    print("ARK 续航与太阳能仿真报告")
    print("=" * 60)
    print()

    # 1. 纯电池续航
    print("## 1. 纯电池续航估算（无太阳能）")
    print(f"电池容量: {BATTERY_ENERGY_WH:.1f} Wh")
    for mode, power in POWER_MODELS.items():
        hours = estimate_runtime(power)
        print(f"  {mode:20s}: {power:5.1f}W -> {hours:6.1f} 小时")
    print()

    # 2. 太阳能充电估算
    print("## 2. 太阳能充电估算（晴天）")
    for panel, power in SOLAR_PANELS.items():
        print(f"  {panel:10s} 太阳能板: 实际充电 {power:.1f}W（考虑 60% 转换效率）")
    print()

    # 3. 中度使用场景
    print("## 3. 中度使用场景（每天 20 次 AI 推理 + 30 分钟阅读）")
    # 每次 AI 推理 ~30 秒 @ 7W
    ai_daily_wh = 20 * (30 / 3600) * 7
    reading_daily_wh = 0.5 * 1.5  # 30 分钟
    idle_daily_wh = 23 * 0.5  # 剩余 23 小时待机
    total_daily = ai_daily_wh + reading_daily_wh + idle_daily_wh
    print(f"  日耗电量: {total_daily:.2f} Wh")
    print()

    # 4. 自持天数
    print("## 4. 离线自持天数（中度使用场景）")
    for panel, solar_w in SOLAR_PANELS.items():
        days = estimate_self_sustain_days(solar_w, total_daily)
        if days == float('inf'):
            print(f"  +{panel:10s} 太阳能板: 无限自持（日发电 ≥ 日耗电）")
        else:
            print(f"  +{panel:10s} 太阳能板: {days:5.1f} 天")
    print()

    # 5. 能量平衡模拟
    print("## 5. 能量平衡模拟（单日）")
    for panel, solar_w in SOLAR_PANELS.items():
        result = simulate_day(solar_w, [
            (12, 0.5),   # 12 小时待机
            (0.5, 1.5),  # 30 分钟阅读
            (1/6, 7.0),  # 20 次 AI 推理，每次 30 秒
        ])
        status = "✅ 自持" if result['self_sustaining'] else "⚠️ 需补充"
        print(f"  {panel:10s}: 消耗 {result['consumption_wh']:.1f}Wh | 发电 {result['solar_generation_wh']:.1f}Wh | "
              f"净 {result['net_wh']:+.1f}Wh | {status}")
    print()


if __name__ == '__main__':
    print_report()
