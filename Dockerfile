#Android development environment based on gcr.io/tensorflow
# version 0.0.1

# Start with Ubuntu 14.04 LTS.
FROM docker.io/whole/tensorflow:latest

RUN sudo dpkg --add-architecture i386
RUN sudo apt-get -qqy update
RUN sudo apt-get -qqy install libncurses5:i386 libstdc++6:i386 zlib1g:i386

WORKDIR /opt
# Install android sdk
RUN curl https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -o android-sdk_r24.4.1-linux.tgz 
RUN tar xzf android-sdk_r24.4.1-linux.tgz ;
RUN ln -s android-sdk-linux android-sdk;
RUN rm android-sdk_r24.4.1-linux.tgz ;
RUN echo y | android-sdk-linux/tools/android update sdk -a --no-ui --filter platform-tools,build-tools-23.0.2,android-23;

# Install Android NDK
RUN curl http://dl.google.com/android/repository/android-ndk-r10e-linux-x86_64.zip -o android-ndk.zip;
RUN unzip -q android-ndk.zip;
RUN ln -s android-ndk-r10e android-ndk;
RUN rm android-ndk.zip;

WORKDIR /tensorflow