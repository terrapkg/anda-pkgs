rpm.global("commit", gh_commit("Ultramarine-Linux/polycrystal"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}