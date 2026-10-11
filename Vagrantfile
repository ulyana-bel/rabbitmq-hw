VAGRANTFILE_API_VERSION = "2"
ENV['VAGRANT_SERVER_URL'] = 'https://elab.pro'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "hw-net1" do | p |
    p.vm.box = 'ubuntu/22.04'
    p.vm.host_name = "hw-net1"
    # Задаем фиксированный IP-адрес для первой ноды
    p.vm.network "private_network", ip: "192.168.56.11"

    p.vm.provider :virtualbox do |res|
      res.customize ["modifyvm", :id, "--cpus", "1"]
      res.customize ["modifyvm", :id, "--memory", "2000"]
    end
  end

  config.vm.define "hw-net2" do | b |
    b.vm.box = 'ubuntu/22.04'
    b.vm.host_name = "hw-net2"
    # Задаем фиксированный IP-адрес для второй ноды
    b.vm.network "private_network", ip: "192.168.56.12"

    b.vm.provider :virtualbox do |res|
      res.customize ["modifyvm", :id, "--cpus", "1"]
      res.customize ["modifyvm", :id, "--memory", "2000"]
    end
  end
  
end
