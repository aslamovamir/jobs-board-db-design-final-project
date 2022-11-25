class QueryHelper:

    # method to convert an SQL tuple to a list of dictionary items
    def ConvertTupleToDict(query: list[tuple()], dictKeys: list[str]) -> list[dict()]:
        # validate the lists
        if query == None or dictKeys == None or len(query) == 0 or len(dictKeys) == 0:
            return None
        # validate that the size of the tuple is the same as that of keys
        if len(query[0]) != len(dictKeys):
            return None

        try:
            # final output
            output = []

            for i in range(1, len(query)):
                convertedRow: dict() = {}
                for j in range(len(dictKeys)):
                    convertedRow[dictKeys[j]] = query[i][j]
                output.append(convertedRow)
    
            return output

        except Exception as e:
            print("\nFailure! ConvertTupleToDict method in QueryHelper failed for some reason.\n",
                f"Please address the following exceptionL: {e}")

        