Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.hostname = "checkNanterre"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.provider "virtualbox" do |vb|
      vb.name = "check_nanterre_server"
      vb.memory = "1024"
  end
   config.vm.provision "shell", path: 'scripts/install.sh'
end
