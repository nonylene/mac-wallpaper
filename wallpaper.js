function run(argv) {
  if (argv.length !== 1) {
    throw Error("usage: osascript -l JavaScript wallpaper.js <filename>")
  }
  var se = Application("System Events")
  se.desktops().forEach(function(desktop) {
    desktop.picture.set(argv[0]);
  })
}
