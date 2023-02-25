# Supported devices

<label>
  Manufacturer:
  <select id="manufacturer"></select>
</label>
<br>
<label>
  Model:
  <select id="model"></select>
</label>

Can boot Depthboot: <b id="deviceDepthboot"></b><br>
Audio support: <b id="deviceAudio"></b><br>
Other issues: <span id="deviceComment"></span>

<span id="deviceInfo"></span>

<script>
export default {
  mounted() {
    import('/device-support/model-select.js').then((module) => {
      module.initDeviceSupport();
    });
  }
}
</script>
