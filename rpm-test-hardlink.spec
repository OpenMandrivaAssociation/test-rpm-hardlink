Name:      test-rpm-hardlink
Version:   1.5
Release:   1
Summary:   Testing hardlink functionality in RPM
License:   MIT

BuildArch: noarch

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cd %{buildroot}%{_datadir}/%{name}

mkdir -p x/y/z

echo "b content" > b

# Create a sparse 4GB file
truncate -s 4G bigfile

# Hardlink group #1
echo "hello1" > c
ln c a

# Hardlink group #2
echo "hello2" > e
ln e f

# Hardlink group #3
echo "triple" > g
ln g h
ln g i

# Zero-size file
touch emptyfile

# Forward symlink
echo "later" > laterfile
ln -s laterfile earlylink

# Symlink
ln -s b d

# Nested file
echo "nested" > x/y/z/file

%files
%dir %{_datadir}/%{name}

# Hardlink group #1
%attr(0640, 1011, 1011) %{_datadir}/%{name}/a
%attr(0640, 1011, 1011) %{_datadir}/%{name}/c

# Normal file
%attr(0600, 0, 0) %{_datadir}/%{name}/b

# Sparse file
%attr(0644, 2022, 2022) %{_datadir}/%{name}/bigfile

# Symlink
%attr(0777, 0, 0) %{_datadir}/%{name}/d

# Hardlink group #2
%attr(0660, 3033, 3033) %{_datadir}/%{name}/e
%attr(0660, 3033, 3033) %{_datadir}/%{name}/f

# Zero-size file
%attr(0440, 0, 0) %{_datadir}/%{name}/emptyfile

# Ghost file
%ghost %attr(0400, 4044, 4044) %{_datadir}/%{name}/ghostfile

# Forward symlink
%{_datadir}/%{name}/earlylink
%{_datadir}/%{name}/laterfile

# Hardlink group #3 (3 links)
%attr(0664, 7077, 7077) %{_datadir}/%{name}/g
%attr(0664, 7077, 7077) %{_datadir}/%{name}/h
%attr(0664, 7077, 7077) %{_datadir}/%{name}/i

# Nested directories
%dir %attr(0750, 5055, 5055) %{_datadir}/%{name}/x
%dir %attr(0750, 5055, 5055) %{_datadir}/%{name}/x/y
%dir %attr(0750, 5055, 5055) %{_datadir}/%{name}/x/y/z
%attr(0644, 6066, 6066) %{_datadir}/%{name}/x/y/z/file

# Character devices
%attr(0600, root, root) %dev(c, 1, 3) /dev/null-test
%attr(0600, root, root) %dev(c, 5, 1) /dev/console-test

# Block devices
%attr(0600, root, root) %dev(b, 8, 0) /dev/sda-test
%attr(0600, root, root) %dev(b, 65, 0) /dev/nvme0n1-test
