project pkg {
  rpm {
    spec = "ivsc-firmware.spec"
  }
  arches = ["x86_64"]
  labels {
        weekly = 1
    }
}
