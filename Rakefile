
MAIN = "app.py"
DEVEL = false


task default: %i[clean build]

desc "Generates setup.py file"
task "setup" do
  sh "py2applet --make-setup app.py"
end

desc "Builds .app file"
task :build do
  sh "/usr/bin/python setup.py py2app #{"-A" if DEVEL}"
end

desc "Clean"
task :clean do
  rm_rf %w[build dist]
end
