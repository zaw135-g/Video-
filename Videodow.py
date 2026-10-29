import yt_dlp

def download_video(url):
    # ဒေါင်းလုဒ်လုပ်ရန်အတွက် Configuration သတ်မှတ်ခြင်း
    ydl_opts = {
        'format': 'best', # အကောင်းဆုံးအရည်အသွေးကို ရွေးချယ်မည်
        'outtmpl': '%(title)s.%(ext)s', # ဗီဒီယိုအမည်အတိုင်း သိမ်းဆည်းမည်
    }
    
    try:
        print("ဗီဒီယိုကို ဒေါင်းလုဒ်ဆွဲနေပါပြီ... ခေတ္တစောင့်ဆိုင်းပေးပါ။")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ ဒေါင်းလုဒ်လုပ်ခြင်း အောင်မြင်ပါပြီ!")
    except Exception as e:
        print(f"❌ အမှားအယွင်း ဖြစ်ပေါ်သွားis: {e}")

if __name__ == "__main__":
    print("=== Python Video Downloader ===")
    video_url = input("ດေါင်းလုဒ်လုပ်လိုသော Video URL ထည့်ပါ: ").strip()
    
    if video_url:
        download_video(video_url)
    else:
        print("⚠️ ကျေးဇူးပြု၍ မှန်ကန်သော URL ထည့်ပါ။")
