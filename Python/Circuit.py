from LogicGate import AndGate, Connector, NandGate, NorGate, NotGate, OrGate

if __name__ == '__main__':

    while True:
        g1 = AndGate("G1")
        g2 = NandGate("G2")
        g3 = NotGate("G3")
        g4 = OrGate("G4")
        g5 = OrGate("G5")
        g6 = NorGate("G6")
        g7 = NandGate("G7")
        c1 = Connector(g1, g5)
        c2 = Connector(g2, g5)
        c3 = Connector(g3, g6)
        c4 = Connector(g4, g6)
        c5 = Connector(g5, g7)
        c6 = Connector(g6, g7)

        print(g7.getOutput())

        answer = input("again?")
        if answer == 'n':
            break
        else:
            print("---------------------------------")
