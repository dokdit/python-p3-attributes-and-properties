#!/usr/bin/env python3



class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"]

    def __init__(self,name="",job=""):
        self.set_name(name)
        self.set_job(job)

    def get_name(self):
        return self._name

    def set_name(self,name):
        
        if isinstance(name, str) and len(name)>0 and len(name)<26:
            name=name.title()
            self._name = name
        else:
            print( "Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self,job):
        if job in self.APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")


    name =property(get_name,set_name,)
    job=property(get_job,set_job,)
        