project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "gstreamer1-plugins-bad.spec"
    }
  labels {
        extra = 1
    }
}
