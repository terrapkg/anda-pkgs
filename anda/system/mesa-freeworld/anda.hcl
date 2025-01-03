project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "mesa-freeworld.spec"
    }
    labels {
        updbranch = 1
    }
}
