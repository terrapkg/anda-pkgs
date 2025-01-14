project pkg {
  rpm {
  arches = ["x86_64"]
    spec = "gstreamer1-plugin-icamerasrc.spec"
  }
  labels {
        weekly = 1
    }
}
