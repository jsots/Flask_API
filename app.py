from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase("dragrace", 
                        user = "justinsotolongo", 
                        password="", 
                        host="localhost", 
                        port="5432")

class BaseModel(Model):
    class Meta:
        database = db

class DragQueen(BaseModel):
    name = CharField()
    season = IntegerField()
    year = IntegerField()

db.connect()
db.drop_tables([DragQueen])
db.create_tables([DragQueen])

DragQueen(name='BeBe Zahara Benet', season=1, year=2009).save()
DragQueen(name='Tyra Sanchez', season=2, year=2010).save()
DragQueen(name='Raja', season=3, year=2011).save()
DragQueen(name='Sharon Needles', season=4, year=2012).save()
DragQueen(name='Jinkx Monsoon', season=5, year=2013).save()
DragQueen(name='Bianca Del Rio', season=6, year=2014).save()
DragQueen(name='Violet Chachki', season=7, year=2015).save()
DragQueen(name='Bob the Drag Queen', season=8, year=2016).save()
DragQueen(name='Sasha Velour', season=9, year=2017).save()
DragQueen(name='Aquaria', season=10, year=2018).save()
DragQueen(name='Yvie Oddly', season=11, year=2019).save()
DragQueen(name='Jada Essence Hall', season=12, year=2020).save()
DragQueen(name='Simone', season=13, year=2021).save()
DragQueen(name='Willow Pill', season=14, year=2022).save()
DragQueen(name='Sasha Colby', season=15, year=2023).save()

app = Flask(__name__)

@app.route('/dragqueens', methods=['GET', 'POST'])
@app.route('/dragqueens/<id>', methods=['GET', "PUT", 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(DragQueen.get(DragQueen.id == id)))
        else:
            queen_list = []
            for queen in DragQueen.select():
                queen_list.append(model_to_dict(queen))
            return jsonify(queen_list)
    
    if request.method == 'POST':
        new_queen = dict_to_model(DragQueen, request.get_json())
        new_queen.save()
        return jsonify({"success": True})
    
    if request.method == 'PUT':
        body = request.get_json()
        DragQueen.update(body).where(DragQueen.id == id).execute()
        return f"Drag Queen {id} has been updated."
    
    if request.method == "DELETE":
        DragQueen.delete().where(DragQueen.id == id).execute()
        return f"Drag Queen {id} has been deleted."
        

@app.route('/')
def index():
    return "I love Drag Race!"

app.run(port=9000, debug=True)