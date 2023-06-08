""" This is more effective on nested dict s. Moreover, if you want to pretty 
print json quickly from a file then you can simply do:"""

cat file.json | python -m json.tool

""" Profiling a script
This can be extremely helpful in pinpointing the bottlenecks in your scripts:
"""
python -m cProfile my_script.py
