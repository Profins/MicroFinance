from django.conf.urls import patterns, include, url

urlpatterns = patterns('micro_admin.views',

    url(r'^$', 'index', name='microadmin_index'),
    url(r'^login/$', 'user_login', name='login'),
    url(r'^createbranch/$', 'create_branch', name='createbranch'),
    url(r'^createclient/$', 'create_client', name='createclient'),
    url(r'^createuser/$', 'create_user', name='createuser'),
    url(r'^creategroup/$', 'create_group', name='creategroup'),
    url(r'^editbranch/(?P<branch_id>\d+)/$', 'edit_branch', name='editbranch'),
    url(r'^edituser/(?P<user_id>\d+)/$', 'edit_user', name='edituser'),
    url(r'^editclient/(?P<client_id>\d+)/$', 'edit_client', name='editclient'),
    url(r'^branchprofile/(?P<branch_id>\d+)/$', 'branch_profile', name='branchprofile'),
    url(r'^userprofile/(?P<user_id>\d+)/$', 'user_profile', name='userprofile'),
    url(r'^clientprofile/(?P<client_id>\d+)/$', 'client_profile', name='clientprofile'),
    url(r'^groupprofile/(?P<group_id>\d+)/$', 'group_profile', name='groupprofile'),
    url(r'^userslist/$', 'users_list', name='userslist'),
    url(r'^viewbranch/$', 'view_branch', name='viewbranch'),
    url(r'^groupslist/$', 'groups_list', name='groupslist'),
    url(r'^viewclient/$', 'view_client', name='viewclient'),
    url(r'^deletebranch/(?P<branch_id>\d+)/$', 'delete_branch', name='deletebranch'),
    url(r'^deleteuser/(?P<user_id>\d+)/$', 'delete_user', name='deleteuser'),
    url(r'^deletegroup/(?P<group_id>\d+)/$', 'delete_group', name='deletegroup'),
    url(r'^deleteclient/(?P<client_id>\d+)/$', 'delete_client', name='deleteclient'),
    url(r'^assignstaff/(?P<group_id>\d+)/$', 'assign_staff_to_group', name='assignstaff'),
    url(r'^addmember/(?P<group_id>\d+)/$', 'addmembers_to_group', name='addmember'),
    url(r'^viewmembers/(?P<group_id>\d+)/$', 'viewmembers_under_group', name='viewmembers'),
    url(r'^removemember/(?P<group_id>\d+)/(?P<client_id>\d+)/$', 'removemembers_from_group', name='removemember'),
    url(r'^updateclientprofile/(?P<client_id>\d+)/$','update_clientprofile',name='updateclientprofile'),
    url(r'^groupmeetings/(?P<group_id>\d+)/$','group_meetings',name='groupmeetings'),
    url(r'^addgroupmeeting/(?P<group_id>\d+)/$','add_group_meeting',name='addgroupmeeting'),
    url(r'^clientsavingsapplication/(?P<client_id>\d+)/$', 'client_savings_application', name='clientsavingsapplication'),
    url(r'^clientsavingsaccount/(?P<client_id>\d+)/$', 'client_savings_account', name='clientsavingsaccount'),
    url(r'^groupsavingsapplication/(?P<group_id>\d+)/$','group_savings_application',name='groupsavingsapplication'),
    url(r'^groupsavingsaccount/(?P<group_id>\d+)/$','group_savings_account',name='groupsavingsaccount'),
    url(r'^approvesavings/(?P<savingsaccount_id>\d+)/$','approve_savings',name='approvesavings'),
    url(r'^rejectsavings/(?P<savingsaccount_id>\d+)/$','reject_savings',name='rejectsavings'),
    url(r'^closesavings/(?P<savingsaccount_id>\d+)/$','close_savings',name='closesavings'),
    url(r'^withdrawsavings/(?P<savingsaccount_id>\d+)/$','withdraw_savings',name='withdrawsavings'),
    url(r'^groupsavingstransactions/(?P<savingsaccount_id>\d+)/$','group_savings_transactions',name='groupsavingstransactions'),
    url(r'^grouploanapplication/(?P<group_id>\d+)/$','group_loan_application',name='grouploanapplication'),
    url(r'^grouploanaccount/(?P<group_id>\d+)/$','group_loan_account',name='grouploanaccount'),
    url(r'^clientsavingstransaction/(?P<savingsaccount_id>\d+)/(?P<client_id>\d+)/$', 'clientsavingstransaction', name='clientsavingstransaction'),
    url(r'^clientloanapplication/(?P<client_id>\d+)/$', 'client_loan_application', name='clientloanapplication'),
    url(r'^approveloan/(?P<loanaccount_id>\d+)/$','approve_loan',name='approveloan'),
    url(r'^rejectloan/(?P<loanaccount_id>\d+)/$','reject_loan',name='rejectloan'),
    url(r'^closeloan/(?P<loanaccount_id>\d+)/$','close_loan',name='closeloan'),
    url(r'^withdrawloan/(?P<loanaccount_id>\d+)/$','withdraw_loan',name='withdrawloan'),
    url(r'^grouploantransactions/(?P<loanaccount_id>\d+)/$','group_loan_transactions',name='grouploantransactions'),
    url(r'^logout/$', 'user_logout', name="logout"),

)