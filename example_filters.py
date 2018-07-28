
# *** these filters do NOT see ping messages, nor do routers see them ***
# *** global imports are NOT accessible, do imports in __init__ and bind them to an attribute ***

class Filters(Base):
    def __init__(self):
        # nice_colors:
        self.colors = {
            "red": (255,0,0),
            "green": (0,255,0),
            "blue": (0,0,255),
            "white": (255,255,255)
        }
        # some imports used
        self.random = __import__("random")
        
    def covert_msg_incoming(self, msg, con):
        ## example to indicate incoming ant
        #if msg.get_type() == "ACO_ant":
            ## do something meaningful here
            #pass    #logger.error("received ant %s" % msg["id"])
        
        ## example to indicate incoming returning ant
        #if msg.get_type() == "ACO_ant" and msg["returning"]:
            ## do something meaningful here
            #pass    #logger.error("returning ant coming from peer %s" % con.get_peer_id())
        pass

    def covert_msg_outgoing(self, msg, con):
        ## example to indicate outgoing ant
        #if msg.get_type() == "ACO_ant":
            ## do something meaningful here
            #pass    #logger.error("sending out ant %s" % msg["id"])
        
        ## example to indicate outgoing returning activating ant
        #if msg.get_type() == "ACO_ant" and msg["returning"] and msg["activating"]:
            ## do something meaningful here
            #pass    #logger.error("sending returning and activating ant to peer %s" % con.get_peer_id())
        pass

    def msg_incoming(self, msg, con):
        self.logger.info("*********** INCOMING(%s) channel %s connection %s ***********" % (msg.get_type(), msg["channel"], con))
        self.leds[2].on(self.colors["red"], 0.5)

    def msg_outgoing(self, msg, con):
        self.logger.info("*********** OUTGOING ***********")
        self.leds[3].on(self.colors["blue"], 0.5)
        if self.router.__class__.__name__ == "Flooding" and self.router.master[msg["channel"]]:
            return False
        #drop = self.random.choice([True, False])
        #if drop:
            #self.leds[1].on(self.colors["white"], 0.5)
        #return drop     # this will drop the message in 50% of the cases
