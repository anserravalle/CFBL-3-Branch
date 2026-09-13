# The asset library

## Division of labor

Niki supplies what only she can: her face, her team, her space, and real video. This system supplies everything else, including objects, atmosphere, nature, texture, and all design and copy.

That line is also the authenticity rule. A carousel can close on a real photograph of Niki and still use a generated still life of a spice drawer, because the drawer is not her and not her property. It can never use a generated clinician, office, session, or client, because those are.

## Google Drive, the raw library

Root: **Marketing** `1mNWKWoZl_B5MS13KcrKpdSBE5ISJtrSR`

| Folder | ID | Holds |
|---|---|---|
| Photo | `1Est0AVqQUe1NfyXE6jeCGNyaK8MjtJZY` | Niki and general shots |
| Headshot | `1_S1ZJamZaqZg_oew-lYJckHNE_GNLHiI` | Staff portraits, feeds the Spotlight series |
| Video | `1EdPF2ymbn4MYEggUGSOVmbndrcPzA_My` | Clips, b-roll, atmospheric motion |
| Property | `1ljrKiDtqDTobRid-ddrHez1bDPqIPQzT` | Office, entry, exterior, grounds, signage |
| Content Library | `1FVEbxXVJHlrJAZR0PvgzrNh8QozxpGwO` | Finished assets |
| Used | `1f_6EcID3VscoqSGdIRt-wBIbFyZ37ZmM` | Source files already published |

## The Used folder rule

**After a piece goes out, move its source files from Photo, Headshot, Video, or Property into Used.** Set by Niki, 2026-08-16.

Anything in Used is available for repurposing into a different piece with a different job, but is never pulled as fresh material for a new week. This is what prevents the same waiting-room clip and the same portrait quietly becoming the whole feed.

Do the move at cycle close, alongside updating the Content rows. Record which files moved in the cycle row so the trail survives.

`create_file` and `update_file` can move files by changing the parent. Deletion is never required and never appropriate here.

## Naming

Pulls match on names. Headshots by the person's name. Photos and clips with a rough date and a word or two, `20260816_waiting_room_warm`.

Unnamed camera-roll files still work but force guesswork, and there are currently a lot of them, `IMG_6528.MOV` through `IMG_6753.MOV`. When a batch arrives unnamed, preview a sample, then propose names rather than asking Niki to rename dozens of files by hand.

**Watch for duplicates across folders.** As of the first load, several clips sit in both Video and Property with identical sizes, for example `IMG_6528`, `IMG_6529`, `IMG_6530`, `IMG_6531`, `IMG_6538`, `IMG_6677`. Treat them as one asset. Moving one copy to Used means moving both.

**HEIC files need converting** before use. Property currently holds several.

## Direction of travel

**Drive to workspace is reliable.** Search, read, pull, build. This is the direction weekly production depends on.

**Workspace to Drive is awkward for large media.** Uploading a full-resolution image means inlining the whole file. Finished art therefore lands on the Content Pipeline record and in chat, and reaches Drive when Niki saves it or when her desktop app is connected. Never quietly downgrade a file to make an upload fit.

**Video pulls but is heavy.** Short clips are fine. Multi-hundred-megabyte `.MOV` files should be sampled rather than fully pulled unless genuinely needed.

## Canva

Four brand kits are reachable: Niki Serravalle's Team `kAFyY1XTC7Y`, cfbl institute `kAHJ1YJ0bj4`, MUSA `kAHMFB7bPAs`, Center for Balanced Living `kAHNmLXRp04`.

Images that live only inside a Canva design cannot be pulled out as source files. Anything needed as raw material must also exist in Drive.

## Adobe: what is and is not reachable

The **Adobe for creativity** connector is already installed and is the single connector covering Photoshop, Lightroom, Express, InDesign, and Illustrator. There is no separate Photoshop or Lightroom connector to add, and adding another Adobe connector does not unlock more image editing.

**Available:** auto-tone, exposure, highlights, lights, darks, shadows, brightness, contrast, Lab white balance, vibrance and saturation, per-channel saturation, HSL and targeted recolor, auto-straighten, crop and resize, generative expand, lens blur, gaussian blur, grain, subject and prompt-based masking, background removal, vectorize.

**Not available, do not promise it:** hair and flyaway retouching, object or person removal, blemish and wrinkle work, background replacement by prompt, photo compositing, upscaling, and generative face or body editing. Those need Photoshop or Firefly directly, or the desktop bridge.

## The standard grading pass

Every real photograph is graded before it reaches a layout. Auto-straighten if needed, then `image_apply_auto_tone`, then `image_apply_adjustments` for highlight recovery, shadow lift, Lab warming, and vibrance. Mask the subject when it needs to separate from the room. One grade across the week's set so mixed sources read as one shoot.

**Outfit and background recoloring is authorized.** Staff have given permission, which means one sitting yields a terracotta version for the practice and a forest version for the Institute without re-shooting. Mask with `image_select_by_prompt` using `bodyParts` of `Coat`, `Upper Clothes`, or `Dress`, then shift hue with the HSL group. Use `colorize` only on neutral, white, gray, or patterned garments.

**The line that does not move:** lighting, color, tone, straightening, depth, crop, and clothing color are fair game. Reshaping a real person's face or body is not.

## Where not to look

**CFBL STAFF in Drive is a personnel folder.** Credentialing trackers, evaluations, insurance, contracts, departure emails. Marketing material never comes from there, even when a usable headshot sits inside it.
