sudo apt install git
sudo apt install cmake
sudo apt install cmake-curses-gui
sudo apt install libasound2-dev

wget https://github.com/poanchen/marsyas/archive/version-0.5.1.tar.gz
tar xvzf version-0.5.1.tar.gz
cd marsyas-version-0.5.1/
mkdir build
cd build
ccmake ../ #(First, select c to configure. And then, select g to generate and exit.)
make -j 3 #(or higher if you have more cores) (This will take quite a bit of time to build it)

cd bin
./HelloWorld #(Ctrl+C to force shut down or similar)
cd ..

sudo apt install swig 
sudo apt install python-dev (the python headers) 
sudo apt install python-matplotlib 
sudo apt install ipython
sudo apt install libfreetype6-dev

ccmake ../ #(First, press enter with up and down arrow to enable the WITH_SWIG and WITH_PNG option to be ON. And then, select g to generate and exit.)
make -j 3 #(or higher if you have more cores) (This will take quite a bit of time to build it)
sudo make install #(Install the Marsyas python bindings so that Python can find them globally)
sudo ldconfig /usr/local/lib #(Add /usr/local/lib to the path searched for libraries)

cd src/marsyas_python 
python windowing.py