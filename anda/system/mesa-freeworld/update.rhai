if !labels.branch.starts_with("f") {
    print(`mesa-freeworld: unsupported branch: ${labels.branch}`);
    terminate();
}
let release = labels.branch.to_upper();
let ver = get(`https://bodhi.fedoraproject.org/updates/?search=mesa&status=stable&releases=${release}&rows_per_page=1&page=1`).json().updates[0].title;
rpm.global("ver", find(`^mesa-([\d.]+)`, ver, 1));
