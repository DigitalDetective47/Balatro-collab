--- STEAMODDED HEADER
--- MOD_NAME: Balatro Collab
--- MOD_ID: BALXBAL
--- MOD_AUTHOR: [Kitty (Kittyknight. on discord)]
--- MOD_DESCRIPTION: Finally, Balatro is collaborating with the hit indie game Balatro

SMODS.Atlas{
            key = "balatro_hearts_1",
            path = "balatro_hearts_1.png",
            px = 71,
            py = 95,
            atlas_table = "ASSET_ATLAS"
        }
SMODS.Atlas{
            key = "balatro_hearts_2",
            path = "balatro_hearts_2.png",
            px = 71,
            py = 95,
            atlas_table = "ASSET_ATLAS"
        }

SMODS.Atlas{
            key = "balatro_spades_1",
            path = "balatro_spades_1.png",
            px = 71,
            py = 95,
            atlas_table = "ASSET_ATLAS"
        }

SMODS.Atlas{
            key = "balatro_spades_2",
            path = "balatro_spades_2.png",
            px = 71,
            py = 95,
            atlas_table = "ASSET_ATLAS"
        }

SMODS.DeckSkin{
            key = "balatro_hearts",
            suit = "Hearts",
            ranks =  {"Jack", "Queen", "King"},
            lc_atlas = "balatro_hearts_1",
            hc_atlas = "balatro_hearts_2",
            loc_txt = {
				["en-us"] = "Balatro Hearts"
			},
            posStyle = "collab"
        }

SMODS.DeckSkin{
            key = "balatro_spades",
            suit = "Spades",
            ranks =  {"Jack", "Queen", "King"},
            lc_atlas = "balatro_spades_1",
            hc_atlas = "balatro_spades_2",
            loc_txt = {
				["en-us"] = "Balatro Spades"
			},
            posStyle = "collab"
        }