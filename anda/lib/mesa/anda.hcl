project pkg {
    arches = ["x86_64", "aarch64", "i386"]
        rpm {
		spec = "mesa.spec"
	}
    labels {
        subrepo = "mesa"
    }
    arches = ["x86_64", "i386", "aarch64"]
}
