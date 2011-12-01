Summary:	Various mail-related perl modules
Name:		perl-MailTools
Version:	2.04
Release:	4%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/MailTools/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/MailTools-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl(Date::Format), perl(Date::Parse), perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More), perl(Test::Pod), perl >= 3:5.8.1

%description
MailTools is a set of Perl modules related to mail applications.

%prep
%setup -q -n MailTools-%{version}

# Set up example scripts
cd examples
for file in *.PL; do
	%{__perl} $file
done
%{__chmod} -x *_demo
# Remove example-generation scripts, no longer needed
# It causes warnings from MakeMaker, but we don't care
%{__rm} *.PL
cd -

# Fix character encodings
/usr/bin/iconv -f iso-8859-1 -t utf8 < ChangeLog > ChangeLog.utf8
%{__mv} ChangeLog.utf8 ChangeLog

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
/usr/bin/find %{buildroot} -type f -name .packlist -exec %{__rm} -f {} ';'
/usr/bin/find %{buildroot} -depth -type d -exec /bin/rmdir {} 2>/dev/null ';'
%{__chmod} -R u+w %{buildroot}/*

%check
%{__make} test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README* examples/
%dir %{perl_vendorlib}/Mail/
%doc %{perl_vendorlib}/Mail/*.pod
%{perl_vendorlib}/Mail/*.pm
%dir %{perl_vendorlib}/Mail/Field/
%doc %{perl_vendorlib}/Mail/Field/*.pod
%{perl_vendorlib}/Mail/Field/*.pm
%dir %{perl_vendorlib}/Mail/Mailer/
%{perl_vendorlib}/Mail/Mailer/*.pm
%{_mandir}/man3/Mail::*.3pm*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.04-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 30 2008 Paul Howarth <paul@city-fan.org> 2.04-1
- Update to 2.04

* Tue Apr 15 2008 Paul Howarth <paul@city-fan.org> 2.03-1
- Update to 2.03

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.02-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.02-2
- rebuild for new perl

* Mon Dec  3 2007 Paul Howarth <paul@city-fan.org> 2.02-1
- Update to 2.02
- Remove buildreqs perl(Net::SMTP) and perl(Net::Domain), bundled with perl
- Add buildreqs perl(Date::Format), perl(Date::Parse), perl(Test::More), and
  perl(Test::Pod)
- Remove patch for CPAN RT#20726, now fixed upstream
- Buildreq perl >= 5.8.1
- Tweak files list to mark pod files as %%doc
- Fix character encoding for ChangeLog

* Mon Aug 13 2007 Paul Howarth <paul@city-fan.org> 1.77-2
- Clarify license as GPL v1 or later, or Artistic (same as perl)
- Unexpand tabs in spec file

* Fri May 11 2007 Paul Howarth <paul@city-fan.org> 1.77-1
- Update to 1.77

* Tue Apr 10 2007 Paul Howarth <paul@city-fan.org> 1.76-1
- Update to 1.76
- Add comment text about the patch for fixing CPAN RT#20726
- BuildRequire perl(ExtUtils::MakeMaker) rather than perl-devel

* Thu Mar  8 2007 Paul Howarth <paul@city-fan.org> 1.74-4
- Buildrequire perl-devel for Fedora 7 onwards
- Fix argument order for find with -depth

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 1.74-3
- FE6 mass rebuild

* Fri Jul 28 2006 Paul Howarth <paul@city-fan.org> 1.74-2
- cosmetic spec file changes
- fix CPAN RT#20726 (RH #200450), allowing Mail::Util::read_mbox() to open
  files with weird names

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.74-1
- 1.74.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.73-1
- 1.73.

* Wed Jan 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.72-1
- 1.72.

* Fri Jan  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.71-1
- 1.71.

* Wed Dec 14 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.67-2
- Fix demo scripts.
- Sync with fedora-rpmdevtools' perl spec template.

* Fri Jul  1 2005 Paul Howarth <paul@city-fan.org> - 1.67-1
- update to 1.67 (#161830)
- assume perl_vendorlib is set
- license is same as perl (GPL or Artistic) according to README
- don't include module name in summary
- use macros consistently
- add dist tag

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.66-2
- rebuilt

* Sat Jan 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.66-1
- Update to 1.66.

* Wed Aug 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.64-0.fdr.1
- Update to 1.64, patch applied upstream.
- Bring up to date with current fedora.us Perl spec template.

* Sat Mar 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.61-0.fdr.2
- Add patch to complete test.pm -> testfile.pm change introduced in 1.61.

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.61-0.fdr.1
- Update to 1.61.
- Reduce directory ownership bloat.
- Run tests in the %%check section.

* Thu Sep 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.60-0.fdr.1
- Update to 1.60.
- Install into vendor dirs.
- Spec cleanups.

* Sat Jul 12 2003 Dams <anvil[AT]livna.org> 0:1.58-0.fdr.5
- Package is now noarch

* Fri Jul 11 2003 Dams <anvil[AT]livna.org> 0:1.58-0.fdr.4
- Changed group tag
- Making test in build section

* Tue Jul  1 2003 Dams <anvil[AT]livna.org> 0:1.58-0.fdr.3
- Modified files section

* Tue Jun 17 2003 Dams <anvil[AT]livna.org> 0:1.58-0.fdr.2
- Added forgotten description
- Modified Summary according to Michael Schwendt suggestion
- Modified tarball permissions to 0644

* Sun Jun 15 2003 Dams <anvil[AT]livna.org>
- Initial build.
