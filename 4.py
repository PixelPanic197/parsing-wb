import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Путь к ChromeDriver
chrome_driver_path = "chromedriver.exe"  # Убедитесь, что путь к драйверу правильный

# Список артикулов
product_ids = ['181172681', '70335079', '14662127', '143748309', '67238841', '182733086', '49465800', '50426545', '70061488', '168725080', '14919414', '176080203', '181172682', '14998214', '178793683', '174024291', '143752129', '70061445', '50426540', '169481774', '175902728', '70419950', 
'182755017', '175927947', '177857200', '176879716', '178786017', '49465803', '146474149', '173234043', '180099400', '178790701', '13922288', '143752131', '161632098', '153743482', '50426541', '143643071', '41486071', '240075059', '173999799', '15847944', '221513251', '177857206', '175296582', '70061489', '168725919', '173492950', '174966738', '175897291', '176078326', '173232594', '175927946', '154944556', '143748308', '177817723', '182755018', '227405190', '182755016', '163439107', '173250262', '176874476', '265841134', '159771359', '217911147', '251197107', '155219663', '181311754', '49431543', '158553330', '240075067', '182755015', '192168126', '234903113', '14659364', '173440629', '176010373', '176887856', '175925924', '152313482', '41493350', '158551114', '167732417', '158603108', '176031349', '171274237', '181383433', '175863739', '41486003', '157426789', '168714573', '169480962', '182755020', '262340155', '217911146', '161229030', '232744915', '178803163', '165959382', '165780931', '181330584', '160766152', '173231135', '237237374', '250254188', '173514855', '18883675', '144801675', '250929447', '221447811', '262340173', '178806874', '176025525', '237237515', '236258862', '227395386', '142957440', '67238840', '182733085', '175927948', '251197110', '165956096', '152376638', '177815507', 
'143273392', '174969178', '149532493', '173110363', '262340252', '143752987', '175894751', '173108258', '248797103', '216391704', '143748311', '171375456', '153779027', '149401731', '214858942', '262340224', '165945026', '155402044', '151861681', '140888031', '178835107', '160712634', '174021919', '171231620', '211450256', '140759963', '262340202', '164254016', '163443335', '175179720', '168717652', '217880223', '161235138', '262340227', '166384517', '227389512', '50410269', '234309011', '236258860', '173509138', '174010124', '173999798', '236171939', '173509136', '178875239', 
'175179723', '178803183', '158729642', '220354719', '173580276', '174009025', '168973976', '153541632', '174189179', '170360285', '171274261', '227389501', '163543425', '174988358', '166048630', '262340226', '50426637', '163499906', '211402775', '98450101', '14659371', '174022822', '174939736', '161234399', '8922986', '176146312', '175179708', '137655474', '97745597', '14567081', '174198370', '176025526', '230830693', '250286045', '169528335', '208724786', '174162675', '182755019', '172064512', '173511184', '232744925', '245281061', '178806876', '178941986', '155406177', '237237517', '152377920', '146496838', '234903109', '146495319', '262340174', '230830691', '227389508', '226505887', '227389502', '227382099', '171373998', '158719380', '149231471', '240075064', '174967141', '156996553', '174177954', '262340144', '181312571', '153759017', '236336572', '176969462', '265841159', '241443036', '265841171', '182780954', '186337868', '212948325', '171231527', '163525503', '160700530', '41486030', '137740065', '181348732', '173255233', '173440630', '234940540', '226329330', '13746494', '177817722', '211652029', '237237519', '221513204', '232744909', '227397108', '181192362', '78248716', '178806878', '175997425', '227397107', '144850379', '265841145', '166788781', '147456127', '173299728', '265841122', '175179717', '174010123', '169486238', '162386280', '250929460', '183663026', '176136480', '169509037', '247686918', '173489850', '183662011', '232744913', '176895374', '181353311', '168978968', '50890254', '163495954', '28484472', '250929407', '18611425', '151819121', '59342804', '160752038', '167747735', '149236639', '221513216', '149623988', '233274365', '178789605', '161650348', '172065175', '262340172', '147649953', '262340133', '175889309', '95437470', '211402739', '151700801', '16043692', '171274242', '208932264', '226484471', '247686917', '164114330', '162403332', '262340179', '262340257', '262340263', '262340264', '262340246', '166130945', '182733428', '211402783', '143253665', '262340230', '262340189', '236331260', '262340209', '230835235', '149622354', '151700799', '162360279', '262340218', '175997426', '181331827', '214887463', '230838594', '262340163', '262340266', '174952857', '262340151', '153724943', '262340183', '262340217', '174194283', '262340146', '49435246', '240075069', '236213348', 
'14919417', '238555127', '240075061', '80164594', '41669151', '158717524', '155406176', '183622099', '240075074', '234940547', '165824514', '176075938', '165941636', '173593092', '226335996', '243205891', '176018821', '176075937', '154891780', '157037933', '183633758', '182725381', '262340208', '18529025', '208932257', '227389506', '221447792', '230830692', '178806872', '149196062', '227395361', '50890255', '153537477', '240075075', '234316374', '158104031', '124164249', '234903105', '234903103', '240075073', '236227128', '146479133', '168661116', '236258858', '237243641', '143548365', '15101123', '173596686', '236336573', '155332905', '169534021', '173299730', '178786015', '176075939', '149743616', '178875463', '149401730', '247686897', '227395366', '155401404', '165953718', '168980884', '157045499', '161632099', '158074564', '169482393', '145176668', '221447795', '174004569', '234978983', '144787101', '50424982', '236192264', '20830137', '262340205', '157924531', '156999998', '14283521', '54018487', '221513211', '159584117', '236329545', '160653324', '262340154', '178833328', '221513256', '158126217', '20866572', '236213349', '159676824', '13922284', '241882932', '151700796', '181350173', '174064802', '181342583', '18611778', '155425423', '163696238', '177857203', '221447789', '234940546', '157388009', '173998293', '49445292', '174988406', '209175419', '152442920', '171231493', '20866557', '181313170', '166139207', '208692656', '262340261', '155360176', '165959381', '152378860', '10895521', '149622351', '221555626', '173244517', '144857877', '151637898', '165920279', '214906070', '155351838', '240075060', '54018480', '18880465', '221447808', '174009024', '219796810', '265841140', '160472517', '17051439', '14765630', '158709726', '142957442', '182733088', '163901093', '137740071', '221513244', '219764537', '163443918', '152575993', '163543553', '262340118', '60726957', '174987107', '248623515', '158105786', '243205897', '209148960', '18529026', '245476545', '262340251', '158771756', '60677021', '163499908', 
'97847335', '262340162', '14659344', '17293713', '15510292', '171373999', '151673887', '209170126', '234903119', '174950536', '150414529', '153773499', '158718586', '240075071', '149236637', '183662022', '140759962', '158072084', '262340198', '165817635', '58067493', '234903130', '166052019', '174986162', '250645452', '240075068', '137842422', '250929440', '172069256', '76436050', '20866556', '160724110', '152563405', '178955106', '173327909', '157955468', '143426291', '50417863', '209262381', '158777219', '11373385', '8922985', '262340232', '241443025', '54018468', '166390503', '262340139', '173587216', '234940525', '165817632', '250645451', '152538400', '218051947', '159590502', '161647392', '247686919', '169505075', '161632101', '262340211', '238556823', '137838616', '240075066', '173427656', '149735038', '208932274', '208932242', '185931548', '241443018', '262340204', '248613414', '166315091', '173255240', '227400930', '163501219', '14765392', '45408695', '262340159', '174005320', '152491534', '162323401', '178680709', '160537036', '153775401', '166133364', '232744922', '262340166', '160863956', '149743649', '173307534', '262340131', '165982760', '159592265', '245333784', '209157205', '268826016', '243205898', '243205894', '166287677', '167730809', '178685894', '173252892', '157037934', '175002335', '145479927', '166038338', '151819915', '230835233', '156991724', '173228082', '245281060', '241443035', '158131476', '166038339', '174074719', '236253468', '92423414', '165941635', '169486789', '174500546', '176878081', '151870603', '20866566', '168697830', '262340134', '147593344', '149623997', '166215455', '149733503', '183699426', '160761727', '70608665', '159764717', '168935272', '262340160', '149373818', '221447790', '165945025', '64233750', '262340117', '174033418', '227401884', '152541455', '176879718', '174988388', '149733504', '171392258', '149187594', '161202358', '174000929', '237237518', '20866565', '236258861', '262340212', '183622096', '166390505', '145176670', '248620566', '262340259', '172065177', '64233743', '174005317', '262340247', '262340181', '77488881', '165948389', '227395384', '227405189', '262342943', '97848854', '173239999', '173249009', '173233429', '212956200', '241443022', '166391978', '72597447', '250286046', '182839213', '13922317', '151817480', '144174585', '165817637', '208970179', '50890249', '262340167', '158786744', '165941634', '262340171', '262342933', '146479134', '160057809', '145134873', '18880481', '166102305', '54007892', '158396730', '171235854', '168714102', '157060370', '181207968', '262340234', '262340241', '96794006', '153720521', '153756066', '162381890', '174951056', '145112636', '161235679', '174968333', '262340178', '45053587', '14567080', '227395375', '262340161', '262340201', '160723764', '173608442', '265841158', '166036451', '148686269', '14319926', '219813567', '173261152', '262340238', '166036450', '153762722', 
'166139565', '144790343', '262340124', '151865205', '262340148', '262340138', '262340248', '262340123', '262340225', '161233577', '262340203', '20866595', '268826218', '262340157', '262340168', '262340169', '262340186', '262340223', '240075072', '234940543', '238556827', '262340210', '262342926', '168806760', '76884616', '241443011', '232744918', '132600291', '238631810', '55192353', '238556836', '159593463', '57918237', '64233764', '157928064', '158551113', '262340149', '268826018', '166427287', '163699903', '166238424', '161217764', '174051333', '144862360', '157060371', '174989166', '160647052', '159674710', '230823819', '170345397', '48387797', '181325255', '149266155', '163699908', '160730763', '176864109', '166038438', '149189944', '157941321', '166221966', '49445311', '160710794', '137748879', '151874039', '149531060', '171290177', '163420689', '149189601', '70061490', '241443023', '149192556', '174969697', '166791421', '140831798', '70067011', '173259741', '160677400', '92388852', '236213350', '92433172', '166037812', '221447802', '160060144', '163545150', '221513222', '262340207', '144862361', '149232668', '262340221', '227389732', '221461121', '160026311', '262340243', '265841164', '248607173', '209157209', '157036706', '9193098', '158394009', '144710938', '146485198', '287935900', '15520537', '17051441', '262340140', '262340213', '262340136', '262342931', '265842102', '265842082', '262340165', '234903115', '161213518', '262340126', '268826028', '262340242', '55191389', '268826030', '137740067', '47437495', '92361942', '140822578', '16592936', '49435231', '149179398', '72609927', '262340170', '137748887', '174011549', '262340233', '49435226', '14567083', '233271726', '149282416', '102575159', '19950322', '250274285', '174027463', '10582231', '209157208', '265841125', '137748906', '18111651', '265842087', '250281936', '250637390', '265842097', '265841121', 
'265841137', '241443028', '268826015', '268826023', '268826017', '265841130', '241886185', '241889948', '250593216', '50890259', '231417971', '160677399', '150628900', '158551115', '54019732', '262340190', '176072981', '18621141', '169513736', '90741859', '250274283', '61832507', '176010371', '62002670', '176973611', '181391576', '214877443', '245281063', '209186965', '250286047', '59925541', '8694945', '262342928', '35428502', '192168124', '208712268', '8439539', '176893070', '227387766', '14662116', '169453013', '54018485', '175904670', '174174371', '146377699', '66522644', '177781482', '61361342', '41493397', '91724461', '152375647', '67238830', '74431964', '208774846', '208937781', '49462403', '13922278', '100066144', '139806170', '230836856', '227387767', '174028846', '10757740', '234940517', '169462446', '174958439', '173097518', '92391971', '173112389', '166285732', '75444348', '54018481', '245336718', '90033060', '13746502', '262340130', '54018465', '50440441', '175007649', '16043670', '178978913', 
'64242145', '262340194', '164106881', '14068609', '167741067', '15248101', '14283491', '14704855', '19943335', '168693413', '171256742', '174177958', '154717874', '183694891', '48042967', '47437493', '155178072', '30936350', '165869050', '150610825', '208866863', '152355122', '47437488', '70419657', '183622098', '262340239', '262340206']  # Замените на свой список

# Настройки браузера
options = Options()
options.add_argument("--headless")  # Убрать комментарий, если не нужен фоновый режим
options.add_argument("--disable-blink-features=AutomationControlled")

# Инициализация драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Список для хранения данных
data = []

try:
    for product_id in product_ids:
        url = f"https://www.wildberries.ru/catalog/{product_id}/detail.aspx"
        driver.get(url)

        # Подождать загрузку страницы
        time.sleep(5)

        # Поля с значением "Не найдено" по умолчанию
        old_price = "Не найдено"
        final_price = "Не найдено"
        rating = "Не найдено"
        reviews_count = "Не найдено"

        try:
            final_price = driver.find_element(By.CSS_SELECTOR, ".price-block__final-price.wallet").text.strip()
        except Exception:
            print(f"Цена не найдена для артикула {product_id}")

        try:
            old_price = driver.find_element(By.CSS_SELECTOR, ".price-block__old-price span").text.strip()
        except Exception:
            print(f"Старая цена не найдена для артикула {product_id}")

        try:
            rating = driver.find_element(By.CSS_SELECTOR, ".product-page__reviews-icon.address-rate-mini").text.strip()
        except Exception:
            print(f"Оценка не найдена для артикула {product_id}")

        try:
            reviews_count = driver.find_element(By.CSS_SELECTOR, ".product-page__reviews-text.j-product-page-reviews-text").text.strip()
        except Exception:
            print(f"Количество отзывов не найдено для артикула {product_id}")

        # Добавляем данные в список
        data.append([product_id, old_price, final_price, rating, reviews_count])

    # Создание DataFrame и сохранение в Excel
    df = pd.DataFrame(data, columns=["Артикул", "Старая цена", "Текущая цена", "Оценка", "Количество отзывов"])
    df.to_excel("prices_and_reviews.xlsx", index=False)

    print("Данные успешно сохранены в файл prices_and_reviews.xlsx")

finally:
    driver.quit()
