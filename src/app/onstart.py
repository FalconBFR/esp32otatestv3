print("In pointed main.py file")
print("onstart v2 v2 v2 !!!!!!")
def connectToWifiAndUpdate():
    import time, machine, network, gc
    #import app.secrets as secrets
    time.sleep(1)
    print('Memory free', gc.mem_free())

    from .updater.ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        #sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        sta_if.connect("ETHomeMesh", "koda2kko")
        while not sta_if.isconnected():
            print("wifi connection not successful yet")
            pass
    print('network config:', sta_if.ifconfig())
    otaUpdater = OTAUpdater('https://github.com/rdehuyss/micropython-ota-updater', main_dir='app', secrets_file="secrets.py")
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        print("update success")
        machine.reset()
    else:
        del(otaUpdater)
        gc.collect()




connectToWifiAndUpdate()