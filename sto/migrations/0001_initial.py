# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(serialize=False, primary_key=True, db_column=b'CC_ConID')),
                ('location_id', models.IntegerField(db_column=b'CC_CompLocID')),
                ('customer_city', models.CharField(max_length=50, null=True, db_column=b'CC_CustCity', blank=True)),
                ('first_name', models.CharField(max_length=50, db_column=b'CC_Name_First')),
                ('middle_name', models.CharField(max_length=50, null=True, db_column=b'CC_Name_Middle', blank=True)),
                ('last_name', models.CharField(max_length=50, db_column=b'CC_Name_Last')),
                ('email', models.CharField(max_length=255, null=True, db_column=b'CC_Email', blank=True)),
                ('direct_phone', models.CharField(max_length=50, null=True, db_column=b'CC_PhoneDirect', blank=True)),
                ('cell', models.CharField(max_length=50, null=True, db_column=b'CC_Cell', blank=True)),
                ('pager', models.CharField(max_length=50, null=True, db_column=b'CC_Pager', blank=True)),
                ('home_phone', models.CharField(max_length=50, null=True, db_column=b'CC_Home_Phone', blank=True)),
                ('description', models.CharField(max_length=50, db_column=b'CC_Desc')),
                ('extension', models.CharField(max_length=50, null=True, db_column=b'CC_Ext', blank=True)),
                ('birthday', models.DateTimeField(null=True, db_column=b'CC_Birthday', blank=True)),
                ('spouse', models.CharField(max_length=50, null=True, db_column=b'CC_Spouse', blank=True)),
                ('notes', models.TextField(null=True, db_column=b'CC_Notes', blank=True)),
                ('rec_newsletter', models.BooleanField(db_column=b'CC_Rec_Newsletter')),
                ('full_name', models.CharField(max_length=50, db_column=b'CC_Full_Name')),
                ('title_courtesy', models.CharField(max_length=8, db_column=b'CC_Title_Courtesy')),
                ('title_suffix', models.CharField(max_length=8, null=True, db_column=b'CC_Title_Suffix', blank=True)),
                ('cctype', models.CharField(max_length=50, db_column=b'CC_Type')),
                ('status', models.CharField(max_length=10, db_column=b'CC_Status')),
                ('date_last_changed', models.DateTimeField(null=True, db_column=b'CC_DtLastChg', blank=True)),
                ('entered_by', models.CharField(max_length=50, null=True, db_column=b'CC_EnteredBy', blank=True)),
                ('entered_date', models.DateTimeField(null=True, db_column=b'CC_EnteredDate', blank=True)),
                ('modified_by', models.CharField(max_length=50, null=True, db_column=b'CC_ModifiedBy', blank=True)),
                ('modified_date', models.DateTimeField(null=True, db_column=b'CC_ModifiedDate', blank=True)),
                ('no_newsletter', models.NullBooleanField(db_column=b'CC_No_Newsletter')),
                ('prospect', models.NullBooleanField(db_column=b'CC_Prospect')),
            ],
            options={
                'db_table': 'tblS_CustContact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer', models.AutoField(serialize=False, primary_key=True, db_column=b'CustNameID')),
                ('name', models.CharField(max_length=100, primary_key=True, db_column=b'CustName')),
                ('url', models.CharField(max_length=50, null=True, db_column=b'CustWebAddr', blank=True)),
                ('category', models.CharField(max_length=20, null=True, db_column=b'CustCategory', blank=True)),
                ('designfeatures', models.TextField(null=True, db_column=b'CustDesignFeatures', blank=True)),
                ('enteredby', models.CharField(max_length=50, null=True, db_column=b'CustEnteredBy', blank=True)),
                ('created', models.DateTimeField(null=True, db_column=b'CustEnteredDate', blank=True)),
                ('msa', models.CharField(max_length=50, null=True, db_column=b'CustMSA', blank=True)),
                ('msa_details', models.TextField(null=True, db_column=b'CustMSA_Details', blank=True)),
            ],
            options={
                'db_table': 'tblS_Customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocationMaster',
            fields=[
                ('location_id', models.AutoField(serialize=False, primary_key=True, db_column=b'CusLocID')),
                ('addr1', models.CharField(max_length=50, null=True, db_column=b'CLAddr1', blank=True)),
                ('addr2', models.CharField(max_length=50, null=True, db_column=b'CLAddr2', blank=True)),
                ('city', models.CharField(max_length=50, db_column=b'CLCity')),
                ('provstate', models.CharField(max_length=50, db_column=b'CLProvState')),
                ('country', models.IntegerField(db_column=b'CLCountry')),
                ('pczip', models.CharField(max_length=50, null=True, db_column=b'CLPCZip', blank=True)),
                ('fax', models.CharField(max_length=50, null=True, db_column=b'CLFax', blank=True)),
                ('email', models.CharField(max_length=50, null=True, db_column=b'CLEmail', blank=True)),
                ('phone', models.CharField(max_length=50, null=True, db_column=b'CLPhone', blank=True)),
                ('irsnum', models.CharField(max_length=50, null=True, db_column=b'CLIRSNum', blank=True)),
                ('disc', models.IntegerField(null=True, db_column=b'CLDisc', blank=True)),
                ('notes', models.TextField(null=True, db_column=b'CLNotes', blank=True)),
                ('credit_status', models.CharField(max_length=30, null=True, db_column=b'CLCreditStatus', blank=True)),
                ('credit_status_date', models.DateTimeField(null=True, db_column=b'CLCreditStatDate', blank=True)),
                ('bill_office', models.NullBooleanField(db_column=b'CLBillOffice')),
                ('status', models.CharField(max_length=20, db_column=b'CLStatus')),
                ('simply_xref', models.IntegerField(null=True, db_column=b'CLSimplyXRef', blank=True)),
                ('contact_type', models.CharField(max_length=50, db_column=b'ClContactType')),
                ('contact_sub_type', models.CharField(max_length=50, null=True, db_column=b'CLContSubType', blank=True)),
                ('pstexempt', models.CharField(max_length=20, null=True, db_column=b'CLPSTExempt', blank=True)),
                ('gstexempt', models.CharField(max_length=20, null=True, db_column=b'CLGSTExempt', blank=True)),
                ('default_tax_code', models.CharField(max_length=2, null=True, db_column=b'CLDefTaxCode', blank=True)),
                ('bill_to_default', models.IntegerField(null=True, db_column=b'CLBillToDefault', blank=True)),
                ('default_commission_rate', models.FloatField(null=True, db_column=b'CLDefCommRate', blank=True)),
                ('entered_by', models.CharField(max_length=50, null=True, db_column=b'CLEnteredBy', blank=True)),
                ('entered_date', models.DateTimeField(null=True, db_column=b'CLEnteredDate', blank=True)),
                ('modified_by', models.CharField(max_length=50, null=True, db_column=b'CLModifiedBy', blank=True)),
                ('modified_date', models.DateTimeField(null=True, db_column=b'CLModifiedDate', blank=True)),
                ('rank', models.FloatField(null=True, db_column=b'CL_Rank', blank=True)),
                ('peoplefocused', models.CharField(max_length=50, null=True, db_column=b'CL_PeopleFocused', blank=True)),
                ('annual_system', models.IntegerField(null=True, db_column=b'CL_AnnualSystem', blank=True)),
                ('type_of_sites', models.CharField(max_length=50, null=True, db_column=b'CL_TypeofSites', blank=True)),
                ('customer_focus', models.CharField(max_length=50, null=True, db_column=b'CL_CustomerFocus', blank=True)),
                ('big_customers', models.CharField(max_length=50, null=True, db_column=b'CL_BigCustomers', blank=True)),
                ('other_markets', models.CharField(max_length=50, null=True, db_column=b'CL_OtherMarkets', blank=True)),
                ('vendor1', models.CharField(max_length=50, null=True, db_column=b'CL_Vendor1', blank=True)),
                ('vendor2', models.CharField(max_length=50, null=True, db_column=b'CL_Vendor2', blank=True)),
                ('vendor3', models.CharField(max_length=50, null=True, db_column=b'CL_Vendor3', blank=True)),
                ('prospect', models.NullBooleanField(db_column=b'CL_Prospect')),
                ('cust_class', models.CharField(max_length=50, null=True, db_column=b'CL_Cust_Class', blank=True)),
                ('market', models.CharField(max_length=50, null=True, db_column=b'CL_Market', blank=True)),
                ('def_tax', models.CharField(max_length=50, null=True, db_column=b'CL_Def_Tax', blank=True)),
            ],
            options={
                'db_table': 'tblS_CusLocMaster',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='STO',
            fields=[
                ('stid', models.SmallIntegerField(serialize=False, primary_key=True, db_column=b'STID')),
                ('project', models.CharField(max_length=50, null=True, db_column=b'STProjNum', blank=True)),
                ('entrydate', models.DateTimeField(db_column=b'STEntryDate')),
                ('status', models.CharField(max_length=15, null=True, db_column=b'STStatus', blank=True)),
                ('notes', models.TextField(null=True, db_column=b'STNotes', blank=True)),
                ('person_responsible', models.CharField(max_length=20, null=True, db_column=b'STRespPerson', blank=True)),
                ('billing', models.CharField(max_length=10, db_column=b'STBilling')),
                ('hotel', models.IntegerField(null=True, db_column=b'STHotel', blank=True)),
                ('perdiem', models.IntegerField(null=True, db_column=b'STPerDiem', blank=True)),
                ('mileage', models.IntegerField(null=True, db_column=b'STMileage', blank=True)),
                ('travel_hrs', models.IntegerField(null=True, db_column=b'STTravel(hrs)', blank=True)),
                ('sitework_hrs', models.IntegerField(null=True, db_column=b'STSiteWork(hrs)', blank=True)),
                ('on_site_date', models.DateTimeField(null=True, db_column=b'STOn_Site_Date', blank=True)),
                ('tech', models.CharField(max_length=50, null=True, db_column=b'STTech', blank=True)),
                ('billingnotes', models.TextField(null=True, db_column=b'STBillingNotes', blank=True)),
                ('invoicenumber', models.CharField(max_length=15, null=True, db_column=b'STInvoiceNumber', blank=True)),
                ('oldstcustomer', models.CharField(max_length=50, null=True, db_column=b'OLDSTCustomer', blank=True)),
                ('oldstcontact', models.CharField(max_length=50, null=True, db_column=b'OLDSTContact', blank=True)),
                ('billingdate', models.DateTimeField(null=True, db_column=b'STBillingDate', blank=True)),
                ('materials', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STMaterials', blank=True)),
                ('labour', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STLabour', blank=True)),
                ('total', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STTotal', blank=True)),
                ('reference', models.CharField(max_length=50, null=True, db_column=b'STReference', blank=True)),
                ('phone', models.CharField(max_length=50, null=True, db_column=b'STPhone', blank=True)),
                ('add1', models.CharField(max_length=50, null=True, db_column=b'STAdd1', blank=True)),
                ('add2', models.CharField(max_length=50, null=True, db_column=b'STAdd2', blank=True)),
                ('add3', models.CharField(max_length=50, null=True, db_column=b'STAdd3', blank=True)),
                ('city', models.CharField(max_length=50, null=True, db_column=b'STCity', blank=True)),
                ('state', models.CharField(max_length=50, null=True, db_column=b'STState', blank=True)),
                ('stzip', models.CharField(max_length=50, null=True, db_column=b'STZip', blank=True)),
                ('tag', models.CharField(max_length=50, null=True, db_column=b'STTag', blank=True)),
                ('fedid', models.CharField(max_length=50, null=True, db_column=b'STFedID', blank=True)),
                ('cell', models.CharField(max_length=50, null=True, db_column=b'STCell', blank=True)),
                ('email', models.CharField(max_length=50, null=True, db_column=b'STEmail', blank=True)),
                ('ship_prior', models.CharField(max_length=10, null=True, db_column=b'STShipPrior', blank=True)),
                ('ship_cost', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STShipCost', blank=True)),
                ('ship_method', models.CharField(max_length=50, null=True, db_column=b'STShipMethod', blank=True)),
                ('technician_rate', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STTechRate', blank=True)),
                ('travle_rate', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STTravRate', blank=True)),
                ('mileage_rate', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STMileRate', blank=True)),
                ('perdeim_rate', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STPerDeimRate', blank=True)),
                ('hotel_rate', models.DecimalField(null=True, decimal_places=4, max_digits=19, db_column=b'STHotelRate', blank=True)),
                ('action_required', models.CharField(max_length=20, null=True, db_column=b'STActionReq', blank=True)),
                ('schedueld_date', models.DateTimeField(null=True, db_column=b'STSchDate', blank=True)),
                ('country', models.IntegerField(null=True, db_column=b'STCountry', blank=True)),
                ('description', models.TextField(null=True, db_column=b'STDescription', blank=True)),
                ('acknowledge', models.NullBooleanField(db_column=b'STAcknowledge')),
                ('custdesc', models.TextField(null=True, db_column=b'STCustDesc', blank=True)),
                ('customer_po', models.CharField(max_length=34, null=True, db_column=b'STCustPO', blank=True)),
                ('bill_coloc', models.IntegerField(null=True, db_column=b'STBillCoLoc', blank=True)),
                ('bill_contact', models.IntegerField(null=True, db_column=b'STBillContact', blank=True)),
                ('contact', models.IntegerField(null=True, db_column=b'STContact', blank=True)),
                ('project_manager', models.CharField(max_length=50, null=True, db_column=b'STProj_Mgr', blank=True)),
                ('priority', models.CharField(max_length=30, null=True, db_column=b'STPriority', blank=True)),
                ('date_closed', models.DateTimeField(null=True, db_column=b'STCloseDate', blank=True)),
                ('tracking_flag', models.NullBooleanField(db_column=b'STTrackFlag')),
                ('contact2', models.IntegerField(null=True, db_column=b'STContact2', blank=True)),
                ('customer2', models.IntegerField(null=True, db_column=b'STCustomer2', blank=True)),
                ('repcontact', models.IntegerField(null=True, db_column=b'STRepContact', blank=True)),
                ('currency', models.CharField(max_length=3, null=True, db_column=b'STCurr', blank=True)),
                ('st_type', models.CharField(max_length=15, db_column=b'ST_Type')),
                ('st_dla', models.DateTimeField(null=True, db_column=b'ST_DLA', blank=True)),
                ('st_days_att', models.IntegerField(null=True, db_column=b'ST_Days_Att', blank=True)),
                ('terms', models.CharField(max_length=50, null=True, db_column=b'ST_Terms', blank=True)),
                ('taxcode', models.CharField(max_length=2, null=True, db_column=b'ST_TAXCode', blank=True)),
                ('st_commrate', models.FloatField(null=True, db_column=b'ST_CommRate', blank=True)),
                ('stsalescomp', models.IntegerField(null=True, db_column=b'STSalesComp', blank=True)),
                ('tax1', models.FloatField(null=True, db_column=b'ST_Tax1', blank=True)),
                ('tax2', models.FloatField(null=True, db_column=b'ST_Tax2', blank=True)),
                ('county', models.CharField(max_length=50, null=True, db_column=b'ST_County', blank=True)),
                ('commadder', models.FloatField(null=True, db_column=b'STCommAdder', blank=True)),
                ('account_type', models.CharField(max_length=50, null=True, db_column=b'ST_Account_Type', blank=True)),
                ('quote', models.CharField(max_length=50, null=True, db_column=b'ST_Quote', blank=True)),
                ('all_po_sent', models.NullBooleanField(db_column=b'ST_AllPOSent')),
                ('segment', models.CharField(max_length=50, null=True, db_column=b'ST_Segment', blank=True)),
                ('site_type', models.CharField(max_length=50, null=True, db_column=b'ST_Site_Type', blank=True)),
                ('invoice_comment', models.CharField(max_length=100, null=True, db_column=b'ST_Invoice_Comment', blank=True)),
                ('def_gl', models.IntegerField(null=True, db_column=b'ST_Def_GL', blank=True)),
                ('def_dept', models.IntegerField(null=True, db_column=b'ST_Def_Dept', blank=True)),
                ('def_cogs_gl', models.IntegerField(null=True, db_column=b'ST_Def_COGS_GL', blank=True)),
                ('def_cogs_dept', models.IntegerField(null=True, db_column=b'ST_Def_COGS_Dept', blank=True)),
                ('company_to_invoice_from', models.IntegerField(db_column=b'STCompany')),
            ],
            options={
                'db_table': 'tblServiceTask',
                'managed': False,
            },
        ),
    ]
