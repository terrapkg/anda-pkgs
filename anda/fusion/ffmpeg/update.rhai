rpm.version(find(`<small>ffmpeg-([\d.]+?)\.tar\.xz</small>`, get("https://ffmpeg.org/download.html"), 1));

let ffmpeg_ver = get(`https://madoguchi.fyralabs.com/v4/terra${labels.branch}/packages/x265`).json().ver;
open_file("anda/fusion/ffmpeg/VERSION_x265.txt").write(ffmpeg_ver);

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
    print(`ffmpeg: unsupported branch: ${labels.branch}`);
    terminate();
}
let tesseract_ver = get(`https://bodhi.fedoraproject.org/updates/?search=tesseract&status=stable&releases=${release}&rows_per_page=1&page=1`).json().updates[0].title;
open_file("anda/fusion/ffmpeg/VERSION_tesseract.txt").write(tesseract_ver);
