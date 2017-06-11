# Cofre

Cofre is an open source data vault web application that aims to provide secure sensitive data storage.

### How it works
Cofre uses 256-bit AES encryption to encrypt the data on client side and send that to the server.

##### Err... but that's so simple...
It's simple indeed! Cofre shines in the key management scheme!

##### And how does that works?
Each vault has one AES key, and that must be shared between all vault participants (and their devices), so that's is a huge security problem!!!

Cofre uses Shamir Secret Sharing Scheme (SSSS) to split the key between all participants, on the following protocol:
 - Bob wants to create a new vault :)
 - Bob asks to Cofre to create a new vault with an identifier X
 - Cofre creates a new vault with an identifier of X and set Bob as it's owner
 - Cofre then generates a new 256-bit AES key
 - Cofre uses SSSS to generate 8 shares from the key, with a threshold of 4
 - Cofre tells Bob to connect another device in the transaction using the vault identifier X
 - Bob connects his smartphone in the transaction of vault X
 - Cofre gives 2 shares to Bob's first device, 2 shares to Bob's smartphone, and keep 2 shares.
 - Before giving any shares, Cofre logs the share hash, with key creation date and share owner
 - Cofre then store the hash of the remaining 2 shares, store the hashes in a special place, encrypt the shares and give them to Bob
 - Cofre then tells Bob that these last 2 shares are special, and that he should keep it stored in a piece of paper or something like that

##### I'm not getting it yet...
Well, if the threshold of the Secret Sharing is 4, so Bob only needs 4 shares to recover the AES key, so he can recover that using his first device and his secondary device. Each device should have 2 shares, raising the need of at least 2 devices to recover the secret.

##### Okay, now I get it. But what about the other shares?
Let's say Bob wants Alice to have access to the vault X, but Bob couldn't give his shares to Alice, so he needs that Cofre give Alice 4 more shares in order for her to have access to the vault.

The "special" 2 shares that Cofre gave Bob are called "Recovery Shares", which Bob should use whenever he wants to add someone to the vault or has lost his own shares.

With the Recovery Shares, anyone could:
 - Add a new participant to the vault
 - Bans a participant from the vault
 - Recover one or more lost shares
 - Reset the vault key

But it's not possible to use the Recovery Shares in the process of recovering the secret, because they are encrypted with a Cofre secret key, so only Cofre can manage those shares.

##### What about the server shares?
Well, in the case of adding a new participant or banning a participant, Bob should give 2 of his own shares and the 2 Recovery Shares.

But what if Bob lost all his shares? In that case the server could use his own 2 shares together with Bob's Recovery Share to generate more shares and give them to Bob!!!

Besides that, for a vault key reset, it's necessary that the owner give his 6 shares (including the Recovery Shares) and the server will use it's own keys to validate those and generate a new key for Bob.

##### And what about the lost of the Recovery Shares?
In that case, Bob should give his 4 shares to the server, that would generate a new one.

##### But anyone with shares could do that, right?
Right! ... and wrong. When Cofre generates the shares, he stores each share hash with it's corresponding owner and device, so he just checks those information, looking for the owner shares hashes, before doing anything. So, if the hash match with the owner's hashes, it must be Bob's!

##### And wh....
Okay, it's about the banning process. Cofre holds a special "hall of shame" table that he puts every share hash that had some issue (lost, stolen, banned, expired...). So whenever he is asked to do anything with shares, he will check this table first.

##### Last thing, I promise! What about the reset key process?
Reseting the key is like creating a new one (duh!), but the owner of the vault can choose from the participant list who should receive new shares, in the case of rogue participants or compromised ones, and the "hall of shame" table for that vault is cleared. In algorithmic terms:
 - Bob asks for a key reset
 - Bob gives his 6 shares
 - Cofre validate all Bob's shares
 - Cofre get the old key and decrypt all of vault's data
 - Cofre generates a new key
 - Cofre then encrypt all vault data with the new key
 - The protocol described above is used again

### Tech
TODO

### Installation
TODO

### Contibuting
TODO

### License
AGPLv3