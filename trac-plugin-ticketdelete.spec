%define		trac_ver	0.10
Summary:	Ticket and Ticket Change Deletion Plugin
Name:		trac-plugin-ticketdelete
Version:	0
Release:	1
License:	BSD-like
Group:		Applications/WWW
# Source0Download:	http://trac-hacks.org/changeset/latest/ticketdeleteplugin?old_path=/&filename=ticketdeleteplugin&format=zip
Source0:	ticketdeleteplugin.zip
# Source0-md5:	5ea5299648bae63f2ac85c2b0af0fe81
URL:		http://trac-hacks.org/wiki/TicketDeletePlugin
BuildRequires:	python-devel
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small plugin to allow deleting tickets from within Trac. Though I
don't advocate this as a method of dealing with tickets very often, it is a
commonly requested feature, and it is needed on rare occasions (generally
dealing with spam). 

It also supports deleting individual changes, including comments.

%prep
%setup -q -n ticketdeleteplugin

%build
cd %{trac_ver}
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd %{trac_ver}
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	Don't forget to enable ticketdelete in conf/trac.ini:

	[components]
	ticketdelete.* = enabled
EOF
#' - vim
fi

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/ticketdelete
%{py_sitescriptdir}/TracTicketDelete-*.egg-info
