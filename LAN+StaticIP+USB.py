# coding=utf-8
import time
from to_log import to_log
from networkConfig import lan_mode
from dmSupport import get_device_attribute
from configFile import data_for_cases

# 生成LAN+静态IP+USB网络配置二维码
# lan_mode(
#     pr='usb',
#     ip=data_for_cases.get('ip'),
#     mask=data_for_cases.get('mask'),
#     gw=data_for_cases.get('gw'),
#     dns=data_for_cases.get('dns')
# )

# 获取系统当前时间
nowTimestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))

# 获取设备属性
da = get_device_attribute(data_for_cases.get('deviceNo'))

if nowTimestamp[:-3] == da.get('time', 'failed')[:-3]:
    if da.get('persist.net.type') == 'eth' or da.get('persist.net.dhcp') == 'false':
        to_log('LAN+静态IP+USB网络配置成功！')
        to_log('配网方式：'+da.get('persist.net.type'))
        to_log('DHCP：' + da.get('persist.net.dhcp'))
        to_log('IP：' + da.get('sys.net.ip'))
        to_log('MASK：' + da.get('persist.net.mask'))
        to_log('GW：' + da.get('persist.net.gw'))
        to_log('DNS：' + da.get('persist.net.dns1'))
        to_log('MAC：' + da.get('system.net.wifi.mac'))
        if da.get('persist.net.ip') != data_for_cases.get('ip'):
            to_log('配置IP为：' + data_for_cases.get('ip'))
            to_log('实际IP为：' + da.get('persist.net.ip'))
        if da.get('persist.net.mask') != data_for_cases.get('mask'):
            to_log('配置子网掩码为：' + data_for_cases.get('mask'))
            to_log('实际子网掩码为：' + da.get('persist.net.mask'))
        if da.get('persist.net.gw') != data_for_cases.get('gw'):
            to_log('配置网关为：' + data_for_cases.get('gw'))
            to_log('实际网关为：' + da.get('persist.net.gw'))
        if da.get('persist.net.dns1') != data_for_cases.get('dns'):
            to_log('配置DNS为：' + data_for_cases.get('dns'))
            to_log('实际DNS为：' + da.get('persist.net.dns1'))
    else:
        to_log('\n请检查断言参数\n')
else:
    to_log('\nLAN+静态IP+USB网络配置失败！\n')

