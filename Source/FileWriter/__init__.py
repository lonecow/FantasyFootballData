
def WriteFullList(Data, FileName):
    fd = open(FileName, 'w')

    fd.write('Player,Position,Team,Var,Owner\n')
    for item in Data:
        fd.write('%s,%s,%s,%.4f,%s\n' % (item['name'], item['pos'], item['team'], float(item['var']), item['owner']))

    fd.close()


'''93 lines per page
   Landscape
   Small margins'''
def WriteByPosition(Data, FileName):
    def _IncrementRow(Row, Column):
        Row += 1

        if Row == 70:
            Column += 6
            Row = 1

        return (Row, Column)

    count = 0
    lists_by_pos = {}
    for item in Data:
        count += 1

        item['pos'] = str(item['pos']).replace(',', '_')
        if item['pos'] not in lists_by_pos:
            lists_by_pos[item['pos']] = []

        item['count'] = count
        lists_by_pos[item['pos']].append(item)



    row = 1
    column = 1
    data = []
    for pos in lists_by_pos:
        pos = pos.replace(',', '_')
        if len(data) < row:
            data.append('** %s **,,,,,,' %(pos))
            (row, column) = _IncrementRow(row, column)
            data.append('Count,Player,Position,Team,Var,Owner,')
            (row, column) = _IncrementRow(row, column)
        else:
            data[row - 1] += ('** %s **,,,,,,' %(pos))
            (row, column) = _IncrementRow(row, column)
            data[row - 1] += 'Count,Player,Position,Team,Var,Owner,'
            (row, column) = _IncrementRow(row, column)

        for item in lists_by_pos[pos]:
            for key in item:
                item[key] = str(item[key]).replace(',', '_')
            
            if len(data) < row:
                data.append('%s,%s,%s,%s,%.2f,%s,' % (item['count'],item['name'], item['pos'], item['team'], float(item['var']), item['owner']))
            else:
                data[row - 1] += '%s,%s,%s,%s,%.2f,%s,' % (item['count'],item['name'], item['pos'], item['team'], float(item['var']), item['owner'])

            (row, column) = _IncrementRow(row, column)

    fd = open(FileName, 'w')
    for item in data:
        fd.write('%s\n' % (item))
    fd.close()
