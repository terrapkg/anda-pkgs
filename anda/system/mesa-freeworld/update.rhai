import "andax/bump_extras.rhai" as bump;

rpm.global("ver", bump::bodhi("mesa", labels.branch.as_bodhi_ver()));
