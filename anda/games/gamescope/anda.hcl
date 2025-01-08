project pkg {
    arches = ["x86_64", "aarch64", "i386"]
	rpm {
		spec = "gamescope.spec"
	}
	labels {
		subrepo = "extras"
	}
}
