project "pkg" {
    rpm {
        spec = "libva-nvidia-driver.spec"
    }
    arches = ["x86_64", "aarch64", "i386"]
}