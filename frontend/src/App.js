import "./App.css";
import {
  Alert,
  Box,
  Button,
  Typography,
  Snackbar,
  TextField,
  InputAdornment,
} from "@mui/material";
import { useEffect, useState } from "react";
import SearchIcon from "@mui/icons-material/Search";
import Minisearch from "minisearch";
import FlagEditor from "./FlagEditor";

function App() {
  const [SBOpen, setSBOpen] = useState(false);
  const [SBMessage, setSBMessage] = useState("");
  const [SBSeverity, setSBSeverity] = useState("info");
  const [FFlags, setFFlags] = useState([
    {
      behaviour: "X",
      name: "Loading...",
      type: "bool",
    },
  ]);

  const [checkedItems, setCheckedItems] = useState({});
  const [textValues, setTextValues] = useState({});

  const handleCheckboxChange = (index) => (event) => {
    setCheckedItems({ ...checkedItems, [index]: event.target.checked });
  };

  const handleTextChange = (index) => (event) => {
    setTextValues({ ...textValues, [index]: event.target.value });
  };

  const [profiles, setProfiles] = useState([
    {
      name: "FPS Unlocker",
      flags: {
        FFlagGameBasicSettingsFramerateCap: true,
      },
    },
    {
      name: "Vulkan Renderer",
      flags: {
        FFlagDebugGraphicsDisableMetal: true,
        FFlagDebugGraphicsPreferVulkan: true,
      },
    },
  ]);
  const [Psearch, setPSearch] = useState("");
  const [PSearcher, setPSearcher] = useState(() => {
    return [];
  });
  const [PSearchResults, setPSearchResults] = useState([]);

  const pSearchFunc = (v) => {
    console.log(PSearcher.search(v));
    setPSearchResults(PSearcher.search(v));
  };

  useEffect(() => {
    const a = [];
    profiles.forEach(function (profile, i) {
      a.push({ ...profile, id: i });
    });
    setProfiles(a);

    const tempSearcher = new Minisearch({
      fields: ["name", "flags"],
      idField: "id",
    });
    tempSearcher.addAll(a);
    setPSearcher(tempSearcher);
  }, []);

  function Presets() {
    const applyPreset = function (preset) {
      Object.entries(preset.flags).forEach((flag) => {
        const index = FFlags.findIndex((v) => v.name === flag[0]);
        if (index !== -1) {
          const fflag = FFlags[index];
          if (fflag.type === "bool") {
            setCheckedItems({ ...checkedItems, [index]: flag[1] });
          } else {
            setTextValues({ ...textValues, [index]: flag[1] });
          }
        }
      });
    };

    return (
      <Box
        display={"flex"}
        justifyContent={"center"}
        alignItems={"center"}
        flexDirection={"column"}
        sx={{ p: 3, bgcolor: "#001e41", borderRadius: 5 }}
      >
        <Box display={"flex"} flexDirection={"column"}>
          <Typography variant="h2" sx={{ color: "white" }}>
            Presets
          </Typography>
          <br />
          <TextField
            value={Psearch}
            onChange={(e) => {
              setPSearch(e.target.value);
              pSearchFunc(e.target.value);
            }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
          />
          <Box
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
            flexDirection={"column"}
          >
            {PSearchResults.length > 0
              ? PSearchResults.map((result) => {
                  const profile = profiles[result.id];
                  return (
                    <Box
                      display={"flex"}
                      justifyContent={"center"}
                      alignItems={"center"}
                    >
                      <Typography variant="h6" sx={{ color: "white" }}>
                        {profile.name}
                      </Typography>
                      <Button
                        color="primary"
                        variant="contained"
                        sx={{ m: 1.5 }}
                        onClick={() => {
                          applyPreset(profile);
                        }}
                      >
                        Apply
                      </Button>
                    </Box>
                  );
                })
              : profiles.map((profile) => {
                  return (
                    <Box
                      display={"flex"}
                      justifyContent={"center"}
                      alignItems={"center"}
                    >
                      <Typography variant="h6" sx={{ color: "white" }}>
                        {profile.name}
                      </Typography>
                      <Button
                        color="primary"
                        variant="contained"
                        sx={{ m: 1.5 }}
                        onClick={() => {
                          applyPreset(profile);
                        }}
                      >
                        Apply
                      </Button>
                    </Box>
                  );
                })}
          </Box>
        </Box>
      </Box>
    );
  }

  return (
    <Box style={{ width: "100%", height: "100%" }}>
      <Box
        display={"flex"}
        justifyContent={"center"}
        alignItems={"center"}
        sx={{
          width: "100vw",
          height: "100vh",
        }}
      >
        <FlagEditor
          setSBSeverity={setSBSeverity}
          setSBOpen={setSBOpen}
          setSBMessage={setSBMessage}
          FFlags={FFlags}
          setFFlags={setFFlags}
          checkedItems={checkedItems}
          setCheckedItems={setCheckedItems}
          textValues={textValues}
          setTextValues={setTextValues}
          handleTextChange={handleTextChange}
          handleCheckboxChange={handleCheckboxChange}
        />
        <Presets />
      </Box>
      <Snackbar
        onClose={() => {
          setSBOpen(false);
        }}
        open={SBOpen}
        autoHideDuration={1200}
      >
        <Alert
          severity={SBSeverity}
          variant="filled"
          onClose={() => {
            setSBOpen(false);
          }}
        >
          {SBMessage}
        </Alert>
      </Snackbar>
    </Box>
  );
}

export default App;
