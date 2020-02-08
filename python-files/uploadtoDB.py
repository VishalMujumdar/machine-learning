# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 06:32:50 2020

@author: vismujum
"""

#pip install psycopg2

import psycopg2
import uuid
import csv
#import time
#import datetime
#import date

from datetime import datetime


#myTime = datetime.now()

#myTime
fileName = r'C:\codeRepository\machine-learning\Marketing_Dummy_Data.csv'

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgresadmin")
cur = conn.cursor()
with open (fileName , 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        v_campaign_id = str('cid_'+uuid.uuid4().hex[:12])
        
        # Data Entries for Campaign Details
        v_week = row[0]
        v_fiscal_quarter = row[1]
        v_year = int('20'+((row[1])[3:5]))
        
        #v_quarter = row[1]
        v_sales_channel = row[2]
        v_mc_type = row[3]
        v_industry = row[4]
        v_geo = row[5]
        v_country = row[6]
        v_campaign_theme = row[7]
        v_parent_campaign = row[8]
        v_child_campaign = row[9]
        
        # Data Entries for Marketing Leads
        v_mktleads_id = str('mkid_'+uuid.uuid4().hex[:12])
        v_visits = row[10]
        v_unique_visitors = row[10]
        v_leads = row[12]
        v_mql = row[13]
        v_pipeline_count = row[14]	
        v_opportunity_accounts = row[15]	

        # Data Entries with Spend Details        
        v_spend_id  = str('spid_'+uuid.uuid4().hex[:12])
        v_mc_subscriptions = row[16]
        v_mc_net_adds = row[17]
        v_mc_billings = row[18]
        v_billings_target = row[19]
        v_pipeline_cost = row[20]
        v_spend = row[21]
        v_budget  = row[22]
        
        # Data entries for Sales Details
        v_sales_id = str('slsid_'+uuid.uuid4().hex[:12])
        v_total_accounts = row[23]
        v_touched_accounts = row[24]
        v_engaged_accounts = row[25]
        v_hi_valued_accounts = row[26]
        v_won_accounts = row[27]	
        v_orders	= row[28]
        v_cart_additions =row[29]	
        v_purchase = row[30]
         
        #Campaign Details
        v_sub_industry = row[31]
        v_sub_industry_2 = row[32]
        
        
        # Marketing Vehicle Performance 
        v_mkgvehicle_id = str('mvhid_'+uuid.uuid4().hex[:12])
        v_product_title = row[33]
        v_product_group = row[34]
        v_product_views = row[35]
        v_vehicle = row[36]
        v_social_website = row[37]
        v_email_number = row[38]
        v_search_engine = row[39]
        v_keyword = row[40]
        v_landing_page = row[41]
        v_device_type = row[42]
        v_video_source = row[43]
        v_video_name = row[44]
        v_display_partner = row[45]
        v_impressions = row[46]
        v_clicks = row[47]
        v_bounces = row[48]
        v_page_views = row[49]
        v_avgtime_spent = row[50]
        v_entries = row[51]
        v_exits = row[52]
        v_email_sent = row[53]
        v_email_clicks   = row[54]
        v_email_delivered = row[55]  
        v_email_opens = row[56]
        v_email_bounces = row[57]
        v_linkedIn_followers = row[58]
        v_linkedIn_new_followers = row[59]
        v_linkedIn_impressions = row[60]
        v_linkedIn_clicks = row[61]
        v_linkedIn_likes = row[62]
        v_facebook_likes  = row[63] 
        v_facebook_page_likes = row[64]
        v_facebook_share  = row[65]
        v_facebook_post_reach  = row[66] 
        v_facebook_interractions = row[67]
        v_facebook_impressions = row[68]
        v_youtube_subscribers = row[69]
        v_youtube_new_subscribers = row[70]
        v_youtube_lifetime_views = row[71]
        v_youtube_comments = row[72]
        v_youtube_likes = row[73]
        v_youtube_share = row[74]
        v_twitter_followers = row[75]
        v_twitter_new_followers  = row[76]
        v_twitter_new_tweets = row[77]
        v_twitter_retweets = row[78]
        v_twitter_mentions = row[79]
        v_twitter_favorites = row[80]
        v_video_views = row[81]
        v_video_25_milestone = row[82]
        v_video_50_milestone = row[83]
        v_video_75_milestone = row[84]
        v_video_completions = row[85]
        v_video_engagement = row[86]
        
        
        # Performance details
        v_perform_id = str('mfid_'+uuid.uuid4().hex[:12])
        v_leads_lastYr = row[87]
        v_avg_pageLoadTime = row[88]
        v_spend_lastYr = row[89]
        v_hivalue_engagedAc_lastYr = row[90]
        v_mc_billings_lastYr = row[91]	
        v_opportunity_acc_lastYr = row[92]
        v_engaged_acc_lastYr = row[93]
        v_pipeline_lastYr = row[94]
        v_won_acc_lastYr = row[95]
        v_mql_lastYr = row[96]
        v_leads_lastYr = row[97]
        v_visits_lastYr = row[98]
        v_unique_visitors_lastYr = row[99]
        v_cart_additions_lastYr = row[100]
        v_subscriptions_lastYr = row[101]
        v_orders_lastYr = row[102]
		
        v_date_created = datetime.now()
        v_date_last_modified = datetime.now()
        
        #sql = "INSERT INTO campaign_details (year,quarter,week,sales_channel,mc_type,industry,sub_industry,sub_industry_2,geo,country,campaign_theme,parent_campaign,child_campaign,date_created,date_last_modified) VALUES(v_year,v_quarter,v_week,v_sales_channel,v_mc_type,v_industry,v_sub_industry,v_sub_industry_2,v_geo,country,v_campaign_theme,v_parent_campaign,v_child_campaign,v_date_created,v_date_last_modified);"
        #sql = "INSERT INTO campaign_details (campaign_id) VALUES(%s);"
        sql_campaign = "INSERT INTO campaign_details (campaign_id,year,quarter,week,sales_channel,mc_type,industry,sub_industry,sub_industry_2,geo,country,campaign_theme,parent_campaign,child_campaign,date_created,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val_campaign = (v_campaign_id,v_year,v_fiscal_quarter,v_week,v_sales_channel,v_mc_type,v_industry,v_sub_industry,v_sub_industry_2,v_geo,v_country,v_campaign_theme,v_parent_campaign,v_child_campaign,v_date_created,v_date_last_modified,)
        cur.execute(sql_campaign,val_campaign)

        # Insert values into Marketing Details Table
        #sql_mkt_leads = "INSERT INTO marketing_leads (mkt_leads_id,visits,unique_visitor,leads,mql,pipeline_count,opportunity_accounts,date_created,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        #val_mkt_leads = (v_mktleads_id,v_visits,v_unique_visitors, v_leads ,v_mql,v_pipeline_count,v_opportunity_accounts,v_date_created,v_date_last_modified,)
        #cur.execute(sql_mkt_leads,val_mkt_leads)
        
        #Insert into Spend Details
        #sql_spend = "INSERT INTO marketing_leads (spend_id, mc_subscriptions, mc_net_adds, mc_billings, billings_target, pipeline_cost, spend , budget, date_created, date_last_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s);"
        #val_spend = (v_spend_id , v_mc_subscriptions , v_mc_net_adds , v_mc_billings , v_billings_target , v_pipeline_cost , v_spend  , v_budget ,v_date_created,v_date_last_modified,)
        #cur.execute(sql_spend,val_spend)
        
        #Insert into Sales Details
        #sql_sales = "INSERT INTO spend_details (sales_id , total_accounts , touched_accounts , engaged_accounts , hi_valued_accounts , won_accounts , orders , cart_additions	, purchase , date_created, date_last_modified) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s , %s ,%s);"
        #val_sales = (v_sales_id , v_total_accounts , v_touched_accounts , v_engaged_accounts , v_hi_valued_accounts , v_won_accounts , v_orders , v_cart_additions ,v_purchase ,v_date_created,v_date_last_modified,)
        #cur.execute(sql_sales,val_sales)
        
        # Insert into Marketing Vehicle details
        #sql_mvh = "INSERT INTO marketing_vehicle_details( mkgvehicle_id , product_title , product_group , product_views , vehicle , social_website , email_number , search_engine , keyword , landing_page , device_type , video_source , video_name , display_partner ,impressions , clicks , bounces , page_views ,	avgtime_spent , entries , exits ,email_sent, email_clicks , email_delivered , email_opens , email_bounces , linkedIn_followers ,linkedIn_new_followers , linkedIn_impressions	, linkedIn_clicks , linkedIn_likes , facebook_likes , facebook_page_likes , facebook_share , facebook_post_reach , facebook_interractions, facebook_impressions , youtube_subscribers, youtube_new_subscribers , 	youtube_lifetime_views , youtube_comments , youtube_likes , youtube_share , twitter_followers , twitter_new_followers , twitter_new_tweets , twitter_retweets	, twitter_mentions , twitter_favorites , video_views , video_25_milestone , video_50_milestone , video_75_milestone	, video_completions , video_engagement , date_created, date_last_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        #val_mvh = (v_mkgvehicle_id ,v_product_title ,v_product_group , v_product_views , v_vehicle ,v_social_website, v_email_number ,v_search_engine , v_keyword ,v_landing_page ,v_device_type ,v_video_source , v_video_name ,v_display_partner , v_impressions , v_clicks , v_bounces , v_page_views , v_avgtime_spent , v_entries , v_exits , v_email_sent , v_email_clicks , v_email_delivered , v_email_opens ,v_email_bounces , v_linkedIn_followers ,v_linkedIn_new_followers , v_linkedIn_impressions ,v_linkedIn_clicks , v_linkedIn_likes ,v_facebook_likes , v_facebook_page_likes ,v_facebook_share , v_facebook_post_reach , v_facebook_interractions , v_facebook_impressions , v_youtube_subscribers, v_youtube_new_subscribers , v_youtube_lifetime_views , v_youtube_comments , v_youtube_likes , v_youtube_share ,v_twitter_followers , v_twitter_new_followers ,v_twitter_new_tweets , v_twitter_retweets , v_twitter_mentions , v_twitter_favorites ,v_video_views , v_video_25_milestone , v_video_50_milestone , v_video_75_milestone, v_video_completions , v_video_engagement,v_date_created,v_date_last_modified,)
        #conn.commit(sql_mvh,val_mvh)

        # Insert into Performance Details
        #sql_pfm = "INSERT INTO performace_details(perform_id ,leads_lastYr ,avg_pageLoadTime ,spend_lastYr ,hivalue_engagedAc_lastYr ,mc_billings_lastYr ,opportunity_acc_lastYr ,engaged_acc_lastYr ,pipeline_lastYr ,won_acc_lastYr ,mql_lastYr ,leads_lastYr ,visits_lastYr ,unique_visitors_lastYr ,cart_additions_lastYr ,subscriptions_lastYr ,orders_lastYr ,date_created  ,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        #val_pfm = (v_perform_id ,v_leads_lastYr , v_avg_pageLoadTime ,v_spend_lastYr , v_hivalue_engagedAc_lastYr , v_mc_billings_lastYr, v_opportunity_acc_lastYr , v_engaged_acc_lastYr , v_pipeline_lastYr , v_won_acc_lastYr ,v_mql_lastYr , v_leads_lastYr , v_visits_lastYr , v_unique_visitors_lastYr , v_cart_additions_lastYr , v_subscriptions_lastYr , v_orders_lastYr , v_date_created , v_date_last_modified ,)
        #conn.commit(sql_pfm,val_pfm)
        
        # Insert into Look Up Table
        #sql_lkp = "INSERT INTO lookup_table (campaign_id , mktleads_id , spend_id , sales_id , mkgvehicle_id , perform_id) VALUES (%s,%s,%s,%s,%s,%s);"
        #val_lkp = (v_campaign_id , v_mktleads_id , v_spend_id , v_sales_id, v_mkgvehicle_id,v_perform_id,)
        #conn.commit(sql_lkp,val_lkp)
        
cur.close()