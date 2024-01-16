# ------------------------------------------
# BDS 1,0
# Data link capability report
# ------------------------------------------


def me10(overlay_control_capability: int, **kwargs):
    """Encode BDS 1,0 message

    Args:
        overlay_control_capability:
        configuration_flag:
        acas_capability:
        mode_s_subnetwork_version_number:
        enhanced_protocol_indicator:
        mode_s_specific_services_capability:
        uplink_elm_average_throughput_capacity:
        downlink_elm_throughput:
        aircraft_identification_capability:
        squitter_capability_subfield:
        surveillance_identifier_code:
        common_usage_gicb_capability_report:
        hybrid_surveillance:
        acas_resolution_advisory:
        acas_version:
        data_terminal_equipment_status:

    Returns:
        str: 14 hexdigits message
    """


    ovc = overlay_control_capability
    cf = kwargs.get("configuration_flag", 0)
    acas_status = kwargs.get("acas_capability", 0)
    mode_s_version = kwargs.get("mode_s_subnetwork_version_number", 0)
    epi = kwargs.get("enhanced_protocol_indicator", 0)
    mss = kwargs.get("mode_s_specific_services_capability", 0)
    uplink_elm = kwargs.get("uplink_elm_average_throughput_capacity", 0)
    downlink_elm = kwargs.get("downlink_elm_throughput", 0)
    aircraft_id = kwargs.get("aircraft_identification_capability", 0)
    scs = kwargs.get("squitter_capability_subfield", 0)
    sic = kwargs.get("surveillance_identifier_code", 0)
    gicb = kwargs.get("common_usage_gicb_capability_report", 0)
    hs = kwargs.get("hybrid_surveillance", 0)
    ra = kwargs.get("acas_resolution_advisory", 0)
    acas_version = kwargs.get("acas_version", 0)
    dte = kwargs.get("data_terminal_equipment_status", 0)

    if ovc not in (0, 1):
        raise Exception("Overlay control capability must be 0 or 1.")

    if cf not in (0, 1):
        raise Exception("Configuration flag must be 0 or 1.")

    if acas_status not in (0, 1):
        raise Exception("ACAS capability must be 0 or 1.")

    if mode_s_version not in range(0, 6):
        raise Exception("Mode S subnetwork version number must be between 0 and 5.")

    if epi not in (0, 1):
        raise Exception("Enhanced protocol indicator must be 0 or 1.")

    if mss not in (0, 1):
        raise Exception("Mode S specific services capability must be 0 or 1.")

    if uplink_elm not in range(0, 8):
        raise Exception("Uplink ELM average throughput capacity must be between 0 and 7.")

    if downlink_elm not in range(0, 16):
        raise Exception("Downlink ELM throughput must be between 0 and 15.")

    if aircraft_id not in (0, 1):
        raise Exception("Aircraft identification capability must be 0 or 1.")

    if scs not in (0, 1):
        raise Exception("Squitter capability subfield must be 0 or 1.")

    if sic not in (0, 1):
        raise Exception("Surveillance identifier code must be 0 or 1.")

    if hs not in (0, 1):
        raise Exception("Hybrid surveillance indicator must be 0 or 1.")

    if ra not in (0, 1):
        raise Exception("ACAS resolution advisory generation must be 0 or 1.")

    if acas_version not in (0, 1, 2):
        raise Exception("ACAS version must be 0, 1, or 2.")

    if gicb not in (0, 1):
        raise Exception("Common usage GICB capability report must be 0 or 1.")

    if dte not in range(0, 65536):
        raise Exception("Data terminal equipment status must be between 0 and 65535.")

    me_bin = "00010000"
    me_bin += str(cf)
    me_bin += "00000"
    me_bin += str(ovc)
    me_bin += str(acas_status)
    me_bin += "{0:07b}".format(mode_s_version)
    me_bin += str(epi)
    me_bin += str(mss)
    me_bin += "{0:03b}".format(uplink_elm)
    me_bin += "{0:04b}".format(downlink_elm)
    me_bin += str(aircraft_id)
    me_bin += str(scs)
    me_bin += str(sic)
    me_bin += str(gicb)
    me_bin += str(hs)
    me_bin += str(ra)
    me_bin += "{0:02b}".format(acas_version)
    me_bin += "{0:016b}".format(dte)

    me_hex = "{0:014X}".format(int(me_bin, 2))

    return me_hex
