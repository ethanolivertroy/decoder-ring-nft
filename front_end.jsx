import { useState } from 'react';
import axios from 'axios';

function App() {
  const [nftAddress, setNftAddress] = useState('');
  const [embeddedData, setEmbeddedData] = useState('');

  const handleExtract = () => {
    axios.get(`/api/nft/${nftAddress}`)
      .then(response => setEmbeddedData(response.data))
      .catch(error => console.error(error));
  }

  const handleDownload = () => {
    const blob = new Blob([atob(embeddedData)], { type: 'video/mp4' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'embedded.mp4';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  return (
    <div>
      <label htmlFor="nft-address">NFT Address:</label>
      <input type="text" id="nft-address" onChange={e => setNftAddress(e.target.value)} />
      <button onClick={handleExtract}>Extract File</button>
      {embeddedData && (
        <div>
          <video controls>
            <source src={`data:video/mp4;base64,${embeddedData}`} type="video/mp4" />
          </video>
          <button onClick={handleDownload}>Download File</button>
        </div>
      )}
    </div>
  );
}

export default App;
