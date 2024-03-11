import {
  Box,
  Button,
  Checkbox,
  Typography,
  ListItem,
  ListItemText,
  TextField,
  InputAdornment,
} from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";
import { FixedSizeList } from "react-window";
import SearchIcon from "@mui/icons-material/Search";
import Minisearch from "minisearch";

export default function FlagEditor({
  setSBSeverity,
  setSBMessage,
  setSBOpen,
  FFlags,
  setFFlags,
  checkedItems,
  setCheckedItems,
  textValues,
  setTextValues,
  handleTextChange,
  handleCheckboxChange,
}) {
  const client = axios.create({
    baseURL: "http://localhost:39457",
  });
  const [searchResults, setSearchResults] = useState([]);
  const [search, setSearch] = useState("");

  const [searcher, setSearcher] = useState(null);

  const updateFFlags = async () => {
    const resp = await client.get("/getParsedFFLags");
    const resp2 = await client.get("/getConfigFFlags");
    if (resp.data.error) {
      setSBSeverity("error");
      setSBMessage(resp.data.error);
      setSBOpen(true);
    } else {
      const fflags = resp.data.fflags;
      setSBSeverity("success");
      setSBMessage("Successfully updated list of fflags!");
      setSBOpen(true);
      var temp = [];
      fflags.forEach((v, i) => {
        temp.push({
          id: i,
          additionalName: v.name.split(/(?=[A-Z])/).join(" "),
          ...v,
        });
      });

      setFFlags(temp);
      const tempSearcher = new Minisearch({
        fields: ["name", "behaviour", "type", "additionalName", "id"],
        storeFields: ["name", "behaviour", "type", "id"],
      });
      tempSearcher.addAll(temp);
      setSearcher(tempSearcher);

      const currentFFlags = resp2.data.fflags;

      Object.entries(currentFFlags).forEach((v) => {
        const item = temp.find((obj) => obj.name === v[0]);
        const index = item.id;

        if (v[1] === true) {
          checkedItems[index] = v[1];
          setCheckedItems(checkedItems);
        } else {
          textValues[index] = v[1];
          setTextValues(textValues);
        }
      });
    }
  };

  const applyFlags = async () => {
    const body = {};
    const temp = { ...checkedItems, ...textValues };
    Object.entries(temp).forEach((val, index) => {
      body[FFlags[parseInt(val[0])]["name"]] = parseInt(val[1])
        ? parseInt(val[1])
        : val[1];
    });
    const resp = await client.post("/updateFFlags", body);
    if (resp.data.error) {
      setSBSeverity("error");
      setSBMessage(resp.data.error);
      setSBOpen(true);
    } else {
      setSBSeverity("success");
      setSBMessage(resp.data.message);
      setSBOpen(true);
    }
  };

  useEffect(() => {
    updateFFlags();
  }, []);

  const openRoblox = async () => {
    const resp = await client.get("/openRoblox");
    if (resp.data.error) {
      setSBSeverity("error");
      setSBMessage(resp.data.error);
      setSBOpen(true);
    } else {
      setSBSeverity("success");
      setSBMessage("Successfully opened roblox");
      setSBOpen(true);
    }
  };

  const bypassSingleRoblox = async () => {
    const resp = await client.get("/bypassSingleRoblox");
    if (resp.data.error) {
      setSBSeverity("error");
      setSBMessage(resp.data.error);
      setSBOpen(true);
    } else {
      setSBSeverity("success");
      setSBMessage("Successfully bypassed");
      setSBOpen(true);
    }
  };

  const closeRoblox = async () => {
    const resp = await client.get("/closeRoblox");
    if (resp.data.error) {
      setSBSeverity("error");
      setSBMessage(resp.data.error);
      setSBOpen(true);
    } else {
      setSBSeverity("success");
      setSBMessage("Successfully closed roblox");
      setSBOpen(true);
    }
  };

  const searchFunc = (search) => {
    if (search !== "") {
      const results = searcher.search(search);
      console.log("Searching");
      console.log(results);
      setSearchResults(results);
    } else {
      setSearchResults([]);
    }
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
          Flag Editor
        </Typography>
        <br />
        <TextField
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
            searchFunc(e.target.value);
          }}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon />
              </InputAdornment>
            ),
          }}
        />

        <FixedSizeList
          height={500}
          width={600}
          itemCount={
            searchResults.length === 0 ? FFlags.length : searchResults.length
          }
          sx={{
            maxHeight: 300,
            overflow: "auto",
          }}
          itemSize={100}
          overscanCount={5}
        >
          {(props) => {
            const { index, style } = props;
            const fflag = (searchResults.length === 0 ? FFlags : searchResults)[
              index
            ];
            const id = fflag.id;
            return (
              <ListItem
                style={style}
                key={index}
                component="div"
                disablePadding
                secondaryAction={
                  fflag.type === "bool" ? (
                    <Checkbox
                      checked={checkedItems[id] || false}
                      onChange={handleCheckboxChange(id)}
                    />
                  ) : (
                    <TextField
                      value={textValues[id] || ""}
                      onChange={(e) => {
                        if (fflag.type === "int") {
                          if (
                            parseInt(e.target.value) ||
                            e.target.value === ""
                          ) {
                            handleTextChange(id)(e);
                          }
                        } else {
                          handleTextChange(id)(e);
                        }
                      }}
                    />
                  )
                }
              >
                <ListItemText sx={{ color: "white" }}>
                  {fflag.name}
                </ListItemText>
              </ListItem>
            );
          }}
        </FixedSizeList>
      </Box>
      <Box>
        <Button
          color="success"
          variant="contained"
          onClick={openRoblox}
          sx={{
            color: "white",
          }}
        >
          Open Roblox
        </Button>
        <Button
          color="primary"
          variant="contained"
          onClick={applyFlags}
          sx={{
            m: 1,
          }}
        >
          Apply Flags
        </Button>
        <Button
          color="error"
          variant="contained"
          onClick={closeRoblox}
          sx={{
            color: "white",
          }}
        >
          Close Roblox
        </Button>
        <br />
        <Button
          color="secondary"
          variant="contained"
          onClick={bypassSingleRoblox}
          sx={{
            color: "white",
          }}
        >
          Setup Multi-Roblox
        </Button>
      </Box>
    </Box>
  );
}
