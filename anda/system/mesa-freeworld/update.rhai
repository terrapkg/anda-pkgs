let release = labels.branch;
if release.starts_with("el") {
    release.crop(2);
    if release == "10" {
        release = "EPEL-10.0"
    } else {
        release = `EPEL-${release}`;
    }
} else if release.starts_with("f") {
    release = labels.nbranch;
} else {
    print(`mesa-freeworld: unsupported branch: ${labels.branch}`);
    terminate();
}
let ver = get(`https://bodhi.fedoraproject.org/updates/?search=mesa&status=stable&releases=${release}&rows_per_page=1&page=1`).json().updates[0].title;
rpm.global("ver", find(`^mesa-([\d.]+)`, ver, 1));
