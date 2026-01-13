Name:      test-rpm-hardlink
Version:   1.2
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

echo "hello" > c
ln c a

echo "group2" > e
ln e f

touch emptyfile

echo "later" > laterfile
ln -s laterfile earlylink

ln -s b d

echo "nested" > x/y/z/file

%files
%dir %{_datadir}/%{name}

# Hardlink group #1
%{_datadir}/%{name}/a
%{_datadir}/%{name}/c

# Normal file
%{_datadir}/%{name}/b

# Sparse file
%{_datadir}/%{name}/bigfile

# Symlink to b
%{_datadir}/%{name}/d

# Hardlink group #2
%{_datadir}/%{name}/e
%{_datadir}/%{name}/f

# Zero-size file
%{_datadir}/%{name}/emptyfile

# Ghost file
%ghost %{_datadir}/%{name}/ghostfile

# Forward symlink
%{_datadir}/%{name}/earlylink
%{_datadir}/%{name}/laterfile

# Nested directory structure
%dir %{_datadir}/%{name}/x
%dir %{_datadir}/%{name}/x/y
%dir %{_datadir}/%{name}/x/y/z
%{_datadir}/%{name}/x/y/z/file

# Another ghost file, as last
%ghost %{_datadir}/%{name}/ghost-after
