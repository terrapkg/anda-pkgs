project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "legcord-nightly.spec"
	}
	labels {
		nightly = 1
	}
}