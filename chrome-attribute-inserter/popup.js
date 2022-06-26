let applyButton = document.getElementById("btn-apply");
let attributeJSONTextArea = document.getElementById("attribute-json");

applyButton.addEventListener("click", async () => {
  const attributeJSON = attributeJSONTextArea.value;
  chrome.storage.sync.set({ attributeJSON });
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: setAttributes,
  });
});

// The body of this function will be executed as a content script inside the
// current page
function setAttributes() {
  chrome.storage.sync.get("attributeJSON", ({ attributeJSON }) => {
    const inputs = [
      ["crossing", "crossing"],
      ["heading", "heading_acc"],
      ["finishing", "finishing"],
      ["dribbling", "dribbling"],
      ["shortPassing", "short_pass"],
      ["volleys", "volleys"],
      ["curve", "curve"],
      ["freeKick", "fk_acc"],
      ["longPassing", "long_pass"],
      ["ballControl", "ball_control"],
      ["acceleration", "acceleration"],
      ["sprintSpeed", "sprint_speed"],
      ["agility", "agility"],
      ["reactions", "reactions"],
      ["balance", "balance"],
      ["shotPower", "shot_power"],
      ["jumping", "jumping"],
      ["stamina", "stamina"],
      ["strength", "strength"],
      ["longShots", "long_shots"],
      ["aggression", "aggression"],
      ["interceptions", "interceptions"],
      ["positioning", "att_position"],
      ["vision", "vision"],
      ["penalties", "penalties"],
      ["composure", "composure"],
      ["marking", "def_aware"],
      ["standingTackle", "stand_tackle"],
      ["slidingTackle", "slide_tackle"],
      ["gkDiving", "gkDiving"],
      ["gkHandling", "gkHandling"],
      ["gkKicking", "gkKicking"],
      ["gkPositioning", "gkPositioning"],
      ["gkReflexes", "gkReflexes"],
    ];
    const attributes = JSON.parse(attributeJSON);

    inputs.map(([inputName, attributeName]) => {
      const input = document.querySelector(`input[name="${inputName}"]`);
      if (input !== undefined) {
        input.value = attributes[attributeName];
        const event = new Event("change", { bubbles: true });
        input.dispatchEvent(event);
      }
    });
  });
}
