def request(flow):
    # If you use transparent mode, you might want to use pretty_url.
    if flow.request.pretty_url == 'http://www.watarunrun.com:5000/masterpiece':
#         flow.request.replace('benign', 'defective')
        flow.request.replace('defective', 'benign')
