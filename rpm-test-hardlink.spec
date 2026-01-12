Name:      test-rpm-hardlink
Version:   1
Release:   1
Summary:   Testing hardlink functionality in RPM
License:   MIT

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cd %{buildroot}%{_datadir}/%{name}

# Create three files
echo "hello" > a
echo "middle" > b
echo "world" > c

# Make a and c hardlinks
rm c
ln a c

%files
%{_datadir}/%{name}/a
%{_datadir}/%{name}/b
%{_datadir}/%{name}/c
