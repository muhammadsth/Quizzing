import psycopg2


class DBControl:
    def __init__(self):
        # TODO: implement constructor
        pass

    def start_conn(self):
        # TODO: start connection
        pass

    def __del__(self):
        # TODO: implement destructor
        pass

    def end_conn(self):
        # TODO: end connection
        pass

    def insert_question(self, course, data):
        # TODO: insert question into respective table
        pass

    def get_question(self, course, qID):
        # TODO: insert question into respective table
        pass

    def get_all_questions(self, course):
        # TODO: insert question into respective table
        pass

    def get_hard_questions(self, course):
        # TODO: insert question into respective table
        pass
