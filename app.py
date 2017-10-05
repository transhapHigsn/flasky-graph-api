from flask import Flask,jsonify
from sqlalchemy.orm import sessionmaker
from models import engine, Representation
from flask import request

app = Flask(__name__)
app.config['DEBUG'] = True

session = sessionmaker(bind=engine)
session = session()

@app.route('/api/graphs/insert/', methods=['POST'])
def insert():
    data = request.json
    idx = int(data['id'])
    nodes = data['nodes']
    edges = data['edges']
    #print('fetch success')
    try:
        graph = Representation(id = idx, nodes=nodes, edges=edges)
        session.add(graph)
        session.commit()
        idx = graph.id
        msg = "Successful"
        return jsonify(msg = msg, idx=idx)
    except:
        session.rollback()
        msg = "Oops, Maybe some error!"
        return jsonify(msg = msg)

    return jsonify(msg = msg, idx=idx)

@app.route('/api/graphs/select/')
def selectGraph():
    try:
        req = request.json
        idx = req['idx']
        res = session.query(Representation).filter_by(id=idx).first()
        if res:
            graph = {
            "id": res.id,
            "nodes":res.nodes,
            "edges":res.edges,
            }

            return jsonify(msg='Successful', graph=graph)

        else:
            return jsonify(msg="No match")

    except Exception as e:
        print (e)
        return jsonify(msg = "Unsuccessful")

@app.route('/api/graphs/update/')
def updateGraph():
    try:
        req = request.json
        update_id = req['update_id']
        nodes = req['nodes']
        edges = req['edges']
        try:
            print("Updating")
            session.query(Representation).filter_by(id=update_id).\
            update({'nodes':nodes,'edges':edges})
            session.commit()
            print("Updated")
        except Exception as e:
            session.rollback()
            print("Update error", e)

        return jsonify(msg="Successful")
    except:
        return jsonify(msg="Unsuccessful")

@app.route('/api/graphs/delete/')
def deleteGraph():
    try:
        req = request.json
        delete_id = req['delete_id']
        session.query(Representation).filter_by(id=delete_id).delete()
        session.commit()
        return jsonify(msg='Successful')
    except:
        session.rollback()
        return jsonify(msg='Unsuccessful')

if __name__=='__main__':
    app.run()
