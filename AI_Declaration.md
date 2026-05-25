# AI Declaration

AI was used to support debugging and understanding of Python concepts. It helped identify issues with error handling where ValueErrors were being masked by generic file errors, and suggested reporting the actual exception rather than a misleading message. It also suggested improving file-processing feedback by tracking line numbers using enumerate(file, start=1), allowing errors to be reported with the exact line causing the issue:

for lineno, line in enumerate(file, start=1):

AI also assisted with sorting logic when handling missing lap time values. A lambda function using a tuple key was suggested to safely sort valid times while pushing None values to the end, preventing crashes:

key=lambda x: (x[1] is None, x[1])

AI was used as a learning aid in the later labs logbooks to further understand the subject matte, and this support was particularly helpful due to my SpLD and poor working memory.