from TestActionLibrary import A

pd = A()

pd.openBrowser()
pd.login('billing1', 'pass123')
pd.patientRegistration()
pd.logout()
pd.login('pharmacy1', 'pass123')
pd.activatePharmacyCounter()
pd.getPharmacyDashboard()
pd.preSystemPharmacyDashboard()
pd.addPharmacyDeposit(deposit=1000)
pd.getPharmacyDashboard()
pd.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=0, deposit=1000, depositreturn=0, provisional=0, provisionacancel=0)
pd.returnPharmacyDeposit(depositreturn=1000)
pd.preSystemPharmacyDashboard()
pd.getPharmacyDashboard()
pd.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=0, deposit=0, depositreturn=1000, provisional=0, provisionacancel=0)
pd.logout()
pd.closeBrowser()
